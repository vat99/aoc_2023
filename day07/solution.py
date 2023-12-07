
from typing import List, Tuple, Dict
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

    def parse(self, lines: List[str]) -> List[Tuple[str, int]]:
        hands_bids = []
        for line in lines:
            split_line = line.strip().split(" ")
            hands_bids.append((split_line[0], int(split_line[1])))
        return hands_bids
    
    def cton(self, card: str) -> int:
        if card == 'A':
            return 14
        elif card == 'K':
            return 13
        elif card == 'Q':
            return 12
        elif card == 'J':
            return 1
        elif card == 'T':
            return 10
        else:
            return int(card)
    
    def get_counts(self, hand: str) -> Dict[int, int]:
        counts = dict()
        for card in map(self.cton, hand):
            counts[card] = counts.get(card, 0) + 1
        if 1 in counts:
            # edge case for all Jacks
            if counts[1] == 5:
                counts = {14: 5}
            else:
                val = counts.pop(1)
                _, new_key = max(zip(counts.values(), counts.keys()))
                counts[new_key] += val
        return counts
    
    def get_rank(self, hand_bid: str) -> Tuple[Tuple[int, Tuple[int, int, int, int, int]], int]:
        hand = hand_bid[0]
        bid = hand_bid[1]
        full_num = tuple(map(self.cton, hand))
        counts = self.get_counts(hand)
        sorted_values = sorted(counts.values(), reverse=True)
        rank = 0
        if sorted_values == [5]:
            rank = 7
        elif sorted_values == [4, 1]:
            rank = 6
        elif sorted_values == [3, 2]:
            rank = 5
        elif sorted_values == [3, 1, 1]:
            rank = 4
        elif sorted_values == [2, 2, 1]:
            rank = 3
        elif sorted_values == [2, 1, 1, 1]:
            rank = 2
        else:
            rank = 1
        return ((rank, full_num), bid) 
    
    @timing_decorator
    def part01(self, fname: str) -> int:
        hands_bids = self.parse(self.read_input(fname))
        sorted_data = sorted(hands_bids, key=self.get_rank)
        result = 0
        for i, elem in enumerate(sorted_data):
            result += (i+1) * elem[1]
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
    print(solution.part01("input.txt"))