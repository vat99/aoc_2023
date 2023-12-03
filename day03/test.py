import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

parse_digit_cases = [
    (
        ("467..114..", "...*......", "..35..633."),
        [467, 35]
    )
]

@pytest.mark.parametrize(
    "test_case", parse_digit_cases
)
def test_find_part_numbers(solution, test_case):
    assert solution.find_part_numbers(*test_case[0]) == test_case[1]