from leetcode_notebook_generator.web_scraper import scrape_leetcode_problem

from . import problem_expectations


def test_web_scraper():
    for p in problem_expectations:
        print(f"Testing web scraper for problem: {p.title}")
        problem = scrape_leetcode_problem(p.url)
        assert problem.title == p.title
        assert problem.test_cases == p.test_cases
        assert problem.solution_code.rstrip("\n ") == p.solution_code
