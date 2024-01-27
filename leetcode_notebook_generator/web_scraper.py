import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from leetcode_notebook_generator.problem_info import Problem

MAX_SECS = 10
EXPLICIT_WAIT_SECS = 1


def scrape_leetcode_problem(url: str) -> Problem:
    # Load environment variables from .env file
    load_dotenv()

    # Get WebDriver path from environment variable
    chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
    if chrome_driver_path is None:
        print("Can't find chrome driver's path in .env")
        exit(1)
    print("Loaded driver path")

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()

    # Initialize Chrome WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, MAX_SECS)
    print("Initialized Chrome WebDriver")

    # Open the LeetCode site
    print("Getting leetcode site")
    driver.get(url)
    time.sleep(EXPLICIT_WAIT_SECS)

    try:
        # Go through dynamic layout walkthrough
        button = wait.until (
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Enable Dynamic Layout')]"))
        )
        print("Skipping dynamic layout walktrhough")
        button.click()
        button = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@title="Skip"]'))
        )
        button.click()

    except NoSuchElementException:
        # No dynamic layout walkthrough
        pass

    # EXTRACT TITLE ############################################
    print("Extracting title")
    # Get title using css classes (probably suboptimal)
    title_anchor = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.text-label-1.font-medium"))
    )
    title = title_anchor.get_property("textContent")
    print(f"Title is detected to be: {title}")

    # EXTRACT CODE IN TEXT AREA ################################
    print("Changing language")
    reveal_langs_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.rounded.px-1\\.5"))
    )
    reveal_langs_button.click()
    time.sleep(0.2)
    lang_buttons = driver.find_elements(By.CSS_SELECTOR, "div.cursor-pointer.pr-3")
    python_button = None
    for button in lang_buttons:
        try:
            button.find_element(By.XPATH, './/div/div[contains(text(), "Python3")]')
        except Exception as _e:
            continue

        python_button = button
        break

    if python_button:
        python_button.click()
        time.sleep(EXPLICIT_WAIT_SECS)
    else:
        print("Python button not found.")
        exit(1)

    print("Extracting code")
    # Try to get the code inside a div using css selector again
    code_area = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.view-lines.monaco-mouse-cursor-text")
        )
    )
    # Get text in code area
    # ignores comments
    code_lines = list(filter(lambda line: line[0] != "#", code_area.text.split("\n")))
    code = (
        code_lines[0]
        + "\n"
        + "".join(code_lines[1:-1])
        + "\n"
        + code_lines[-1]
        + "pass"
    )
    print(f"Extracted code:\n{code}")

    # EXTRACT TEST CASES #######################################
    # Double click console button to reveal the test cases
    print("Clicking console button")
    console_button = driver.find_element(
        By.XPATH, '//div[@data-layout-path="/c1/ts1/tb0"]'
    )
    action_chains = ActionChains(driver)
    action_chains.double_click(console_button).perform()

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    print("Waiting for test case buttons")
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@data-e2e-locator='console-testcase-tag']")
        )
    )
    print("Extracting test cases")
    test_case_buttons = driver.find_elements(
        By.XPATH, "//button[@data-e2e-locator='console-testcase-tag']"
    )
    print(f"Number of test cases detected to be {len(test_case_buttons)}")

    test_cases = []
    for button in test_case_buttons:
        button_text = button.text
        button.click()

        # Wait for the parameters to load
        time.sleep(EXPLICIT_WAIT_SECS)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")
        # Find all divs that looks like "{name} ="
        names_divs = soup.find_all(
            "div", string=lambda t: t is not None and str(t).strip().endswith("=")
        )

        parameters = {}
        for name_div in names_divs:
            name = name_div.get_text(strip=True).rstrip("= ")
            value = name_div.find_next("div").find("div").get_text(strip=True)
            parameters[name] = value
        test_cases.append(parameters)

        print(f"Parameters for {button_text}: {parameters}")

    # Close the browser
    driver.quit()

    # Return problem object
    return Problem(title=title, test_cases=test_cases, solution_code=code)
