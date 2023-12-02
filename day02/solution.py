# day01: calorie counting
from typing import List, Tuple, Dict
import re
from functools import reduce

class Solution:

    def parse_line(self, line: str) -> Tuple[int, Dict[str, int]]:
        split_line = line.split(":")
        id = split_line[0].split(" ")[1]
        color_counts = dict()
        for cc in re.split(',|;', split_line[1].strip()):
            cc = cc.strip()
            split_cc = cc.split(" ")
            count = int(split_cc[0])
            color = split_cc[1]
            color_counts[color] = max(color_counts.get(color, 0), count)
        return (int(id), color_counts)
    
    def part01(self, fname: str) -> int:
        red_max = 12
        green_max = 13
        blue_max = 14
        lines = self.read_input(fname=fname)
        return reduce(
            lambda x,y: x+y[0] if y[1]['red'] <= red_max and y[1]['green'] <= green_max and y[1]['blue'] <= blue_max else x,
            map(self.parse_line, lines), 
            0,
        )
    
    def part02(self, fname: str) -> int:
        lines = self.read_input(fname=fname)
        return reduce(
            lambda x,y: x+(y[1]['red']*y[1]['green']*y[1]['blue']),
            map(self.parse_line, lines), 
            0,
        )
    
    def read_input(self, fname: str) -> List[List[str]]:
        all_lines = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_lines.append(line.strip())
        return all_lines

if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))