import re

from leetcode_notebook_generator.notebook_generator import generate_notebook
from leetcode_notebook_generator.web_scraper import scrape_leetcode_problem

DESTINATION_DIR = "./output/"


def main():
    while True:
        leetcode_url = input("Enter URL: ")

        # Pattern that matches with url from leetcode domain
        url_pattern = r"(https?:\/\/(.+?\.)?leetcode\.com(\/[A-Za-z0-9\-\._~:\/\?#\[\]@!$&'\(\)\*\+,;\=]*)?)"
        if re.match(url_pattern, leetcode_url):
            break
        else:
            print("Invalid URL. Please try again.")

    print("Scraping from leetcode site")
    problem = scrape_leetcode_problem(leetcode_url)

    print("Generating note book")
    generate_notebook(problem, DESTINATION_DIR)


if __name__ == "__main__":
    main()
