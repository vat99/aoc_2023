import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

input_to_graph = [
    ("sample.txt", (1,1)),
    ("sample2.txt", (1,1)),
    ("sample3.txt", (2,0)),
    ("sample4.txt", (2,0)),
]
@pytest.mark.parametrize(
    "test_case", input_to_graph
)
def test_read_input(solution, test_case):
    assert solution.read_input(test_case[0])[1] == test_case[1]

input_to_graph = [
    ("sample.txt", (1,1), ((1, 2), (2, 1))),
    ("sample.txt", (1,2), ((1, 1), (1, 3))),
    ("sample.txt", (1,3), ((1, 2), (2, 3))),
    ("sample.txt", (2,3), ((1, 3), (3, 3))),
    ("sample.txt", (3,3), ((2, 3), (3, 2))),
    ("sample.txt", (3,2), ((3, 3), (3, 1))),
    ("sample.txt", (3,1), ((3, 2), (2, 1))),
    ("sample.txt", (2,1), ((3, 1), (1, 1))),
]
@pytest.mark.parametrize(
    "test_case", input_to_graph
)
def test_get_connecting_pipes(solution, test_case):
    assert set(solution._find_neighbor_pipes(graph=solution.read_input(test_case[0])[0], loc=test_case[1])) == set(test_case[2])