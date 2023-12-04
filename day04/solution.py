# day01: calorie counting
from typing import List, Tuple, Dict
import re
from functools import reduce

class Solution:

    def get_card_score(self, line: str) -> int:
        split_line = line.split(":")[1].strip().split("|")
        winning_numbers = [int(i) for i in split_line[0].strip().split(" ") if i != ""]
        all_numbers = [int(i) for i in split_line[1].strip().split(" ") if i != ""]
        score = 0
        for winning_number in winning_numbers:
            if winning_number in all_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        return score
    
    def get_matches(self, line: str) -> int:
        split_line = line.split(":")[1].strip().split("|")
        winning_numbers = [int(i) for i in split_line[0].strip().split(" ") if i != ""]
        all_numbers = [int(i) for i in split_line[1].strip().split(" ") if i != ""]
        matches = 0
        for winning_number in winning_numbers:
            if winning_number in all_numbers:
                matches += 1
        return matches
    
    def part01(self, fname: str) -> int:
        return reduce(
            lambda x,line: x+self.get_card_score(line),
            self.read_input(fname),
            0
        )
    
    def part02(self, fname: str) -> int:
        all_lines = self.read_input(fname)
        card_counts = [1 for _ in range(len(all_lines))]
        for i in range(len(card_counts)):
            matches = self.get_matches(all_lines[i])
            for j in range(matches):
                card_counts[i+j+1] += card_counts[i]
        return sum(card_counts)
    
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