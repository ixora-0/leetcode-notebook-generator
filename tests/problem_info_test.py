from leetcode_notebook_generator.problem_info import Problem

from . import problem_expectations


def test_problem_info():
    for p in problem_expectations:
        print(f"Testing problem info for problem: {p.title}")
        problem = Problem(
            title=p.title, test_cases=p.test_cases, solution_code=p.solution_code
        )
        import_code = problem.generate_imports()
        if isinstance(import_code, str):
            assert import_code.rstrip("\n ") == p.import_code
        else:
            assert import_code == p.import_code  # should both be none
        assert problem.get_function_name().strip() == p.function_name
        assert [
            line.strip()
            for line in problem.generate_test_cases().split("\n")
            if line.strip()
        ] == p.test_cases_code_lines
