import argparse
import re

from leetcode_notebook_generator.notebook_generator import generate_notebook
from leetcode_notebook_generator.web_scraper import scrape_leetcode_problem

DEFAULT_DESTINATION_DIR = "./output/"


def is_leetcode_url(url):
    # Pattern that matches with url from leetcode domain
    url_pattern = r"(https?:\/\/(.+?\.)?leetcode\.com(\/[A-Za-z0-9\-\._~:\/\?#\[\]@!$&'\(\)\*\+,;\=]*)?)"
    return re.match(url_pattern, url)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Jupyter Notebook template from leetcode problem URL"
    )
    parser.add_argument("url", nargs="?", help="URL of leetcode problem")
    parser.add_argument(
        "-d",
        "--destination",
        default=DEFAULT_DESTINATION_DIR,
        help=f"Destination directory (default: {DEFAULT_DESTINATION_DIR})",
    )
    args = parser.parse_args()

    if args.url:
        if not is_leetcode_url(args.url):
            print("Can't recognize URL.")
            exit(1)
        leetcode_url = args.url
    else:
        while True:
            leetcode_url = input("Enter URL: ")

            if is_leetcode_url(leetcode_url):
                break
            print("Can't recognize URL. Please try again.")

    print("Scraping from leetcode site")
    problem = scrape_leetcode_problem(leetcode_url)

    print("Generating notebook")
    generate_notebook(problem, args.destination)


if __name__ == "__main__":
    main()
