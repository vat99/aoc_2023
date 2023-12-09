
from typing import List, Tuple, Dict
from functools import reduce
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute")
        return result
    return wrapper

class Solution:

    def parse(self, line: str) -> List[int]:
        return list(map(int, line.strip().split(" ")))
    
    def all_equal(self, line: List[int]) -> bool:
        return all(item == line[0] for item in line)
    
    def get_differences(self, line: List[int]):
        return reduce(
            lambda x, y: x+[y[1]-y[0]],
            zip(line, line[1:]),
            []
        )
    
    def part01(self, fname: str) -> int:
        return sum(map(self.get_extrapolated_value_last, self.read_input(fname)))
    
    def get_extrapolated_value_last(self, line: str) -> int:
        line = self.parse(line)
        all_differences = [line, self.get_differences(line)]
        while not self.all_equal(all_differences[-1]):
            all_differences.append(self.get_differences(all_differences[-1]))
        return reduce(
            lambda x, y: x + y[-1],
            all_differences[::-1],
            0
        )
    
    def get_extrapolated_value_first(self, line: str) -> int:
        line = self.parse(line)
        all_differences = [line, self.get_differences(line)]
        while not self.all_equal(all_differences[-1]):
            all_differences.append(self.get_differences(all_differences[-1]))
        return reduce(
            lambda x, y: y[0]-x,
            all_differences[::-1][1:],
            all_differences[-1][0]
        )
    
    def part02(self, fname: str) -> int:
        return sum(map(self.get_extrapolated_value_first, self.read_input(fname)))
    
    def read_input(self, fname: str) -> List[str]:
        all_lines = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_lines.append(line.strip())
        return all_lines

if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))