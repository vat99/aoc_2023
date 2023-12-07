import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

hand_to_numbers = [
    ("32T3K", [3, 2, 10, 3, 13]),
]

@pytest.mark.parametrize(
    "test_case", hand_to_numbers
)
def test_hand_to_numbers(solution, test_case):
    assert list(map(solution.cton, test_case[0])) == test_case[1]

hand_to_counts = [
    ("32T3K", {3: 2, 2: 1, 10: 1, 13: 1}),
    ("T55J5", {5: 4, 10: 1}),
    ("KTJJT", {10: 4, 13: 1}),
    ("QQQJA", {12: 4, 14: 1}),
    ("JJJJJ", {14: 5}),
]

@pytest.mark.parametrize(
    "test_case", hand_to_counts
)
def test_get_counts(solution, test_case):
    assert solution.get_counts(test_case[0]) == test_case[1]

hand_to_rank = [
    (("32T3K", 765), ((2, (3, 2, 10, 3, 13)), 765)),
    (("T55J5", 684), ((6, (10, 5, 5, 1, 5)), 684)),
    (("KK677", 28), ((3, (13, 13, 6, 7, 7)), 28)),
    (("KTJJT", 220), ((6, (13, 10, 1, 1, 10)), 220)),
    (("QQQJA", 483), ((6, (12, 12, 12, 1, 14)), 483)),
]

@pytest.mark.parametrize(
    "test_case", hand_to_rank
)
def test_get_ranks(solution, test_case):
    assert solution.get_rank(test_case[0]) == test_case[1]

sort_data = [
    (
        [
            ((2, (3, 2, 10, 3, 13)), 765), 
            ((4, (10, 5, 5, 11, 5)), 684), 
            ((3, (13, 13, 6, 7, 7)), 28), 
            ((3, (13, 10, 11, 11, 10)), 220), 
            ((4, (12, 12, 12, 11, 14)), 483),
        ],
        [
            ((2, (3, 2, 10, 3, 13)), 765),
            ((3, (13, 10, 11, 11, 10)), 220),
            ((3, (13, 13, 6, 7, 7)), 28),
            ((4, (10, 5, 5, 11, 5)), 684),
            ((4, (12, 12, 12, 11, 14)), 483),
        ]
    )
]
@pytest.mark.parametrize(
    "test_case", sort_data
)
def test_sort(solution, test_case):
    assert sorted(test_case[0]) == test_case[1]

hand_to_rank = [
    (
        [
            ("32T3K", 765),
            ("T55J5", 684),
            ("KK677", 28),
            ("KTJJT", 220),
            ("QQQJA", 483),
        ],
        [
            ("32T3K", 765),
            ("KK677", 28),
            ("T55J5", 684),
            ("QQQJA", 483),
            ("KTJJT", 220),
        ]
    )
]

@pytest.mark.parametrize(
    "test_case", hand_to_rank
)
def test_get_sorted_order(solution, test_case):
    assert sorted(test_case[0], key=solution.get_rank) == test_case[1]