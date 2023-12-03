# day01: calorie counting
from typing import List, Tuple, Dict
import re
from functools import reduce

class Solution:

    def batch_inputs(self, lines: List[str]) -> List[int]:
        num_lines = len(lines)
        return zip(range(num_lines), range(1, num_lines), range(2, num_lines))
    
    def find_numbers(self, line: str) -> List[Tuple[int, int]]:
        matches = re.finditer(r'(\d+)', line)
        numbers_with_indices = [(match.group(), match.start(), match.end() - 1) for match in matches]
        return numbers_with_indices
    
    def match_intersect_above_below(self, start, end, i) -> bool:
        return (start <= i-1 and i-1 <= end) or (start <= i and i <= end) or (start <= i+1 and i+1 <= end)
    
    def match_intersect_same(self, start, end, i) -> bool:
        return (start <= i-1 and i-1 <= end) or (start <= i+1 and i+1 <= end)
    
    def find_part_numbers(self, prev_line: str, current_line: str, next_line: str) -> List[int]:
        symbols = "!@#$%^&*()-_+=`~/,<>:;|"
        prev_line_matches = self.find_numbers(prev_line)
        current_line_matches = self.find_numbers(current_line)
        next_line_matches = self.find_numbers(next_line)
        part_number_results = []
        for i, c in enumerate(current_line):
            if c in symbols:
                for num, start, end in prev_line_matches+next_line_matches:
                    if self.match_intersect_above_below(start, end, i):
                        part_number_results.append(int(num))
                for num, start, end in current_line_matches:
                    if self.match_intersect_same(start, end, i):
                        part_number_results.append(int(num))
        return part_number_results
    
    def find_gear_numbers(self, prev_line: str, current_line: str, next_line: str) -> List[int]:
        symbols = "*"
        prev_line_matches = self.find_numbers(prev_line)
        current_line_matches = self.find_numbers(current_line)
        next_line_matches = self.find_numbers(next_line)
        total_sum = 0
        for i, c in enumerate(current_line):
            if c in symbols:
                gear_number_matches = []
                for num, start, end in prev_line_matches+next_line_matches:
                    if self.match_intersect_above_below(start, end, i):
                        gear_number_matches.append(int(num))
                for num, start, end in current_line_matches:
                    if self.match_intersect_same(start, end, i):
                        gear_number_matches.append(int(num))
                if len(gear_number_matches) == 2:
                    total_sum += gear_number_matches[0] * gear_number_matches[1]
        return total_sum
    
    def part01(self, fname: str):
        all_lines = self.read_input(fname=fname)
        batched_inputs = self.batch_inputs(all_lines)
        result = 0
        for i, (a, b, c) in enumerate(batched_inputs):
            result += sum(self.find_part_numbers(all_lines[a], all_lines[b], all_lines[c]))
        return result
    
    def part02(self, fname: str):
        all_lines = self.read_input(fname=fname)
        batched_inputs = self.batch_inputs(all_lines)
        result = 0
        for i, (a, b, c) in enumerate(batched_inputs):
            result += self.find_gear_numbers(all_lines[a], all_lines[b], all_lines[c])
        return result
    
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