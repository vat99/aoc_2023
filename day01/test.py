import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

parse_digit_cases = [
    ("1abc2", ("1", "2")),
    ("pqr3stu8vwx", ("3", "8")),
    ("a1b2c3d4e5f", ("1", "5")),
    ("treb7uchet", ("7", "7")),
]

parse_spelled_digit_cases = [
    ("two1nine", ("2", "9")),
    ("eightwothree", ("8", "3")),
    ("abcone2threexyz", ("1", "3")),
    ("xtwone3four", ("2", "4")),
    ("4nineeightseven2", ("4", "2")),
    ("zoneight234", ("1", "4")),
    ("7pqrstsixteen", ("7", "6")),
    ("eightqrssm9httwogqshfxninepnfrppfzhsc", ("8", "9")),
    ("one111jxlmc7tvklrmhdpsix", ("1", "6")),
    ("69sixnine", ("6", "9")),
    ("bvjx5lg5vgrqq", ("5", "5")),
    ("1eightcrcjcbdthreebscfpvznqfrj6", ("1", "6")),
    ("drkdbmv4zbjbznsqtj", ("4", "4")),
    ("8pjkm", ("8", "8")),
    ("tdpxzld5", ("5", "5")),
    ("45", ("4", "5")),
    ("sevenxvbcbsvxr7eighttwo", ("7", "2"))
]

@pytest.mark.parametrize(
    "test_case", parse_digit_cases
)
def test_p1_regex(solution, test_case):
    assert solution.find_first_and_last_digits(test_case[0]) == test_case[1]

@pytest.mark.parametrize(
    "test_case", parse_spelled_digit_cases
)
def test_p2_regex(solution, test_case):
    assert solution.find_first_and_last_digits_spelled(test_case[0]) == test_case[1]

read_input_case = [
    ("sample.txt", ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"])
]

@pytest.mark.parametrize(
    "test_case", read_input_case
)
def test_read_input(solution, test_case):
    assert solution.read_input(test_case[0]) == test_case[1]

p1_case = [
    ("sample.txt", 142)
]

@pytest.mark.parametrize(
    "test_case", p1_case,
)
def test_p1(solution, test_case):
    assert solution.part01(test_case[0]) == test_case[1]

p2_case = [
    ("sample2.txt", 281)
]

@pytest.mark.parametrize(
    "test_case", p2_case,
)
def test_p2(solution, test_case):
    assert solution.part02(test_case[0]) == test_case[1]