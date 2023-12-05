import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

parse_digit_cases = [
    (
        "sample.txt",
        (
            [79, 14, 55, 13],
            [
                [(50, 98, 2), (52, 50, 48)],
                [(0, 15, 37), (37, 52, 2), (39, 0, 15)],
                [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],
                [(88, 18, 7), (18, 25, 70)],
                [(45, 77, 23), (81, 45, 19), (68, 64, 13)],
                [(0, 69, 1), (1, 0, 69)],
                [(60, 56, 37), (56, 93, 4)]
            ]
        )
    )
]

@pytest.mark.parametrize(
    "test_case", parse_digit_cases
)
def test_find_part_numbers(solution, test_case):
    assert solution.parse(test_case[0]) == test_case[1]

unmodified_dict = {x: x for x in range(100)}
modified_dict = {x: x for x in range(98)}
modified_dict.update({98: 50, 99: 51})
test_modify_translation_cases = [
    (
        ([(50, 98, 2), (52, 50, 48)],unmodified_dict),
        modified_dict
    )
]

@pytest.mark.parametrize(
    "test_case", test_modify_translation_cases
)
def test_modify_translation(solution, test_case):
    translation_map, translation_dict = test_case[0]
    solution.modify_translation(translation_map, translation_dict)
    assert translation_dict == test_case[1]