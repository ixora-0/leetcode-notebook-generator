from typing import List, Dict
from dataclasses import dataclass


@dataclass
class ProblemExpectation:
    url: str
    title: str
    test_cases: List[Dict[str, str]]
    solution_code: str
    import_code: str | None
    function_name: str
    test_cases_code_lines: List[str]


problem_expectations = [
    ProblemExpectation(
        url="https://leetcode.com/problems/two-sum/description/",
        title="1. Two Sum",
        test_cases=[
            {"nums": "[2,7,11,15]", "target": "9"},
            {"nums": "[3,2,4]", "target": "6"},
            {"nums": "[3,3]", "target": "6"},
        ],
        solution_code="class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:",
        import_code="from typing import List",
        function_name="twoSum",
        test_cases_code_lines=[
            "S = Solution()",
            "# case 1",
            "nums = [2,7,11,15]",
            "target = 9",
            "print(f'Case 1 outputted {S.twoSum(nums, target)}.')",
            "# case 2",
            "nums = [3,2,4]",
            "target = 6",
            "print(f'Case 2 outputted {S.twoSum(nums, target)}.')",
            "# case 3",
            "nums = [3,3]",
            "target = 6",
            "print(f'Case 3 outputted {S.twoSum(nums, target)}.')",
        ],
    ),
    ProblemExpectation(
        url="https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        title="3. Longest Substring Without Repeating Characters",
        test_cases=[{"s": '"abcabcbb"'}, {"s": '"bbbbb"'}, {"s": '"pwwkew"'}],
        solution_code="class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:",
        import_code=None,
        function_name="lengthOfLongestSubstring",
        test_cases_code_lines=[
            "S = Solution()",
            "# case 1",
            's = "abcabcbb"',
            'print(f"Case 1 outputted {S.lengthOfLongestSubstring(s)}.")',
            "# case 2",
            's = "bbbbb"',
            'print(f"Case 2 outputted {S.lengthOfLongestSubstring(s)}.")',
            "# case 3",
            's = "pwwkew"',
            'print(f"Case 3 outputted {S.lengthOfLongestSubstring(s)}.")',
        ],
    ),
]
