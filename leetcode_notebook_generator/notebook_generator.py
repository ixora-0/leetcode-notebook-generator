import os

import nbformat as nbf

from leetcode_notebook_generator.problem_info import Problem


def generate_notebook(problem: Problem, destination: str):
    # Proccess path
    absolute_destination = os.path.abspath(destination)
    if not os.path.exists(absolute_destination):
        os.makedirs(absolute_destination)
    if not os.path.isdir(absolute_destination):
        print(f"Invalid destination path {destination} ")
        exit(1)
    notebook_name = f"{problem.title.replace('.', '-')}.ipynb"

    # Create a new notebook
    nb = nbf.v4.new_notebook()

    # Add cells to the notebook
    # Problem Title
    problem_title_cell = nbf.v4.new_markdown_cell(f"# {problem.title}")
    nb.cells.append(problem_title_cell)

    # importing types
    import_cell = nbf.v4.new_code_cell(problem.generate_imports())
    nb.cells.append(import_cell)

    # Solution Class
    solution_cell = nbf.v4.new_code_cell(problem.solution_code)
    nb.cells.append(solution_cell)

    # Test Cases
    test_title = nbf.v4.new_markdown_cell("# Tests")
    nb.cells.append(test_title)
    test_case_cell = nbf.v4.new_code_cell(problem.generate_test_cases())
    nb.cells.append(test_case_cell)

    # Save notebook
    with open(os.path.join(destination, notebook_name), "w") as f:
        nbf.write(nb, f)
        print(f'Notebook "{notebook_name}" generated at {destination}')
