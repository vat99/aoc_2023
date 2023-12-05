
from typing import List, Tuple, Dict
import re
from functools import reduce

class Solution:

    def parse(self, fname: str):
        seeds = []
        maps = []
        all_lines = self.read_input(fname)
        seeds = list(map(int, all_lines[0].split(':')[1].strip().split(' ')))
        all_lines = all_lines[2:]
        current_map = []
        for line in all_lines:
            if 'map' in line:
                current_map = []
            elif line == '':
                maps.append(current_map)
            else:
                triple = tuple(map(int, line.strip().split(' ')))
                current_map.append(triple)
        maps.append(current_map)
        return seeds, maps
    
    def modify_translation(self, maps: List[Tuple[int, int, int]], translation: Dict[int, int]):
        update_dict = dict()
        for dest_start, source_start, range_len in maps:
            for i in range(range_len):
                update_dict[source_start+i] = dest_start+i
        translation.update(update_dict)

    def translate_maps(self, num: int, maps: List[Tuple[int, int, int]]):
        for dest_start, source_start, range_len in maps:
            if source_start <= num and num <= source_start+range_len:
                delta = num - source_start
                return dest_start + delta
        return num
    
    def part01(self, fname: str) -> int:
        seeds, maps = self.parse(fname)
        return min([reduce(lambda x, y: self.translate_maps(x, y), maps, s) for s in seeds])
    
    def part02(self, fname: str) -> int:
        seeds, maps = self.parse(fname)
        all_seeds = reduce(lambda x, y: x+list(range(y[0], y[0]+y[1])), zip(seeds[0::2], seeds[1::2]), [])
        print(len(all_seeds))
        return min([reduce(lambda x, y: self.translate_maps(x, y), maps, s) for s in all_seeds])
    
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