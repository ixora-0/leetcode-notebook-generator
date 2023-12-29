import re
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Problem:
    title: str
    test_cases: List[Dict[str, str]]
    solution_code: str

    def generate_imports(self) -> str | None:
        pattern = r"\b(List|Tuple|Dict|Set)\b"
        matches = set(re.findall(pattern, self.solution_code))
        if not matches:
            return None
        return "from typing import " + ", ".join(set(matches))

    def get_function_name(self) -> str:
        pattern = r"def\s+(\w+)\s*\("
        function_name = re.search(pattern, self.solution_code)
        if function_name:
            function_name = function_name.group(1)
        else:
            print("Can't extract function name from solution code:")
            print(self.solution_code)
            exit(1)
        return function_name

    def generate_test_cases(self) -> str:
        test_cases_code = "S = Solution()\n"
        function_name = self.get_function_name()
        for i, params in enumerate(self.test_cases, start=1):
            test_cases_code += f"# case {i}\n"
            param_names = []
            for name, value in params.items():
                param_names.append(name)
                test_cases_code += f"{name} = {value}\n"

            test_cases_code += f"print(f'Case {i} outputted "
            test_cases_code += f"{{S.{function_name}({', '.join(param_names)})}}.')\n"
        return test_cases_code
