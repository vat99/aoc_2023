
from typing import List, Tuple, Dict
import math
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

    def parse(self, lines: List[str]) -> Tuple[str, Dict[str, Tuple[str, str]]]:
        directions = lines[0]
        edges = dict()
        for line in lines[2:]:
            split_line = line.split("=")
            location = split_line[0].strip()
            left_right = split_line[1].strip().split(',')
            left = left_right[0].strip()[1:]
            right = left_right[1].strip()[:-1]
            edges[location] = (left, right)
        return directions, edges
    
    def part01(self, fname: str) -> int:
        directions, edges = self.parse(self.read_input(fname))
        location = 'AAA'
        i = 0
        while location != 'ZZZ':
            current_direction = directions[i % len(directions)]
            location = edges[location][0] if current_direction == 'L' else edges[location][1]
            i += 1
        return i
    
    def part02(self, fname: str) -> int:
        directions, edges = self.parse(self.read_input(fname))
        start_loc = self.get_all_start_end_locations(edges)
        i = 0
        locations = start_loc
        location_steps = [0 for _ in locations]
        while not self.check_location_steps(location_steps):
            current_direction = directions[i % len(directions)]
            i += 1
            for j in range(len(locations)):
                loc = locations[j]
                locations[j] = edges[loc][0] if current_direction == 'L' else edges[loc][1]
                if locations[j].endswith('Z'):
                    location_steps[j] = i
        return math.lcm(*location_steps)
    
    def check_location_steps(self, location_steps: List[int]) -> bool:
        for loc in location_steps:
            if loc == 0:
                return False
        return True
    
    def check_locations(self, locations: List[str]) -> bool:
        for loc in locations:
            if not loc.endswith('Z'):
                return False
        return True
    
    def get_all_start_end_locations(self, edges: Dict[str, Tuple[str, str]]) -> List[str]:
        start_loc = []
        end_loc = []
        for loc in edges.keys():
            if loc.endswith('A'):
                start_loc.append(loc)
        return start_loc
    
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