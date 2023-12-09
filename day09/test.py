import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

line_to_differences = [
    ("0 3 6 9 12 15", [3, 3, 3, 3, 3]),
]
@pytest.mark.parametrize(
    "test_case", line_to_differences
)
def test_hand_to_numbers(solution, test_case):
    line = solution.parse(test_case[0])
    differences = solution.get_differences(line)
    assert differences == test_case[1]

line_to_extrapolated_value_last = [
    ("0 3 6 9 12 15", 18),
    ("1 3 6 10 15 21", 28),
    ("10 13 16 21 30 45", 68),
]
@pytest.mark.parametrize(
    "test_case", line_to_extrapolated_value_last
)
def test_get_extrapolated_value_last(solution, test_case):
    assert solution.get_extrapolated_value_last(test_case[0]) == test_case[1]

line_to_extrapolated_value_first = [
    ("10 13 16 21 30 45", 5),
    ("0 3 6 9 12 15", -3),
    ("1 3 6 10 15 21", 0),
]
@pytest.mark.parametrize(
    "test_case", line_to_extrapolated_value_first
)
def test_get_extrapolated_value_first(solution, test_case):
    assert solution.get_extrapolated_value_first(test_case[0]) == test_case[1]