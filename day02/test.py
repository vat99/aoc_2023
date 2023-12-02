import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

parse_digit_cases = [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (1, {"blue": 6, "red": 4, "green": 2})),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (2, {"blue": 4, "red": 1, "green": 3})),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (3, {"blue": 6, "red": 20, "green": 13}))
]

@pytest.mark.parametrize(
    "test_case", parse_digit_cases
)
def test_p1_regex(solution, test_case):
    assert solution.parse_line(test_case[0]) == test_case[1]