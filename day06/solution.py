
from typing import List, Tuple
import re
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

    def parse(self, lines) -> Tuple[List[str], List[str]]:
        return re.findall(r'\S+', lines[0].split(":")[1].strip()), re.findall(r'\S+', lines[1].split(":")[1].strip())
    
    def part01(self, fname: str) -> int:
        times, distances = self.parse(self.read_input(fname))
        times = map(int, times)
        distances = map(int, distances)
        counts = []
        for time, distance in zip(times, distances):
            count = 0
            for i in range(time):
                calculdated_distance = i * (time - i)
                if calculdated_distance > distance:
                    count += 1
            counts.append(count)
        return reduce(lambda x, y: x*y, counts, 1)
    
    @timing_decorator
    def part02(self, fname: str) -> int:
        times, distances = self.parse(self.read_input(fname))
        time = int(''.join(times))
        distance = int(''.join(distances))
        count = 0
        for i in range(time):
            calculdated_distance = i * (time - i)
            if calculdated_distance > distance:
                count += 1
        return count
    
    @timing_decorator
    def part02_faster(self, fname: str) -> int:
        times, distances = self.parse(self.read_input(fname))
        time = int(''.join(times))
        distance = int(''.join(distances))
        count = 0
        for i in range(time//2 + 1):
            calculdated_distance = i * (time - i)
            if calculdated_distance > distance:
                if i == time // 2 and time % 2 == 0:
                    count += 1
                else:
                    count += 2
        return count
    
    def read_input(self, fname: str) -> List[str]:
        all_lines = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_lines.append(line.strip())
        return all_lines

if __name__ == "__main__":  
    solution = Solution()
    start = time.time()
    print(solution.part02("input.txt"))
    print(solution.part02_faster("input.txt"))