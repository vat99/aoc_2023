# day01: calorie counting
from typing import List, Tuple
import re
from functools import reduce

"""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

yields

12, 38, 15, and 77
"""

class Solution:
    def find_first_and_last_digits_spelled(self, line: str) -> Tuple:
        digit_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        matches = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line)
        first_digit = matches[0]
        last_digit = matches[-1]
        first_digit = digit_dict.get(first_digit) if first_digit in digit_dict else first_digit
        last_digit = digit_dict.get(last_digit) if last_digit in digit_dict else last_digit
        return (first_digit, last_digit)

    def find_first_and_last_digits(self, line: str) -> Tuple:
        first_digit = re.search(r'\d', line)
        last_digit = re.search(r'\d(?=[^\d]*$)', line)
        return (first_digit.group(), last_digit.group())
    
    def part01(self, fname: str) -> int:
        lines = self.read_input(fname=fname)
        return reduce(
            lambda x,y: x+int(y[0]+y[1]),
            map(self.find_first_and_last_digits, lines), 
            0,
        )
    
    def part02(self, fname: str) -> int:
        lines = self.read_input(fname=fname)
        return reduce(
            lambda x,y: x+int(y[0]+y[1]),
            map(self.find_first_and_last_digits_spelled, lines), 
            0,
        )
    
    def read_input(self, fname: str) -> List[List[str]]:
        all_lines = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_lines.append(line.strip())
        return all_lines
    
    def compare(self, fname: str):
        digit_dict = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        lines = self.read_input(fname=fname)
        sum_correct = 0
        sum_incorrect = 0
        for line in lines:
            matches_correct = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line)
            matches_incorrect = re.findall(r'1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine', line)

            first_digit_c = matches_correct[0]
            last_digit_c = matches_correct[-1]
            first_digit_c = digit_dict.get(first_digit_c) if first_digit_c in digit_dict else first_digit_c
            last_digit_c = digit_dict.get(last_digit_c) if last_digit_c in digit_dict else last_digit_c

            first_digit_ic = matches_incorrect[0]
            last_digit_ic = matches_incorrect[-1]
            first_digit_ic = digit_dict.get(first_digit_ic) if first_digit_ic in digit_dict else first_digit_ic
            last_digit_ic = digit_dict.get(last_digit_ic) if last_digit_ic in digit_dict else last_digit_ic
            if (first_digit_c, last_digit_c) != (first_digit_ic, last_digit_ic):
                print(f"line: {line}")
                print(f"correct matches: {(first_digit_c, last_digit_c)}")
                print(f"incorrect matches: {(first_digit_ic, last_digit_ic)}")
                print()

if __name__ == "__main__":
    solution = Solution()
    solution.compare("input.txt")