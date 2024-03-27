
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
    
    def read_input(self, fname: str) -> Tuple[List[str], Tuple[int, int]]:
        all_lines = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            r, c = 0, 0
            for i, line in enumerate(lines):
                stripped_line = line.strip()
                for j, s in enumerate(stripped_line):
                    if s == 'S':
                        r, c = i, j
                all_lines.append(line.strip())

        return all_lines, (r, c)
    
    def _find_neighbor_pipes(self, graph: List[str], loc: Tuple[int, int]) -> Tuple[Tuple[int, int]]:
        r, c = loc
        cur_pipe = graph[r][c]
        match cur_pipe:
            case '|':
                return ((r+1, c), (r-1, c))
            case '-':
                return ((r, c+1), (r, c-1))
            case 'L':
                return ((r-1, c), (r, c+1))
            case 'J':
                return ((r, c-1), (r-1, c))
            case '7':
                return ((r, c-1), (r+1, c))
            case 'F':
                return ((r, c+1), (r+1, c))
            case _:
                matching_pipes = []
                # south: (r+1, c)
                if r+1 < len(graph):
                    if graph[r+1][c] in ('|', 'L', 'J'):
                        matching_pipes.append((r+1, c))
                # north: (r-1, c)
                if r-1 > 0:
                    if graph[r-1][c] in ('|', '7', 'F'):
                        matching_pipes.append((r-1, c))
                # east: (r, c+1)
                if c+1 < len(graph[r]):
                    if graph[r][c+1] in ('-', '7', 'J'):
                        matching_pipes.append((r, c+1))
                # west: (r, c-1)
                if c-1 > 0:
                    if graph[r][c-1] in ('-', 'L', 'F'):
                        matching_pipes.append((r, c-1))
                return tuple(matching_pipes)
            
    def part01(self, fname: str) -> Tuple[int, set, List[str]]:
        graph, loc = self.read_input(fname=fname)
        p1, p2 = self._find_neighbor_pipes(graph=graph, loc=loc) # assuming 2 neighbors from start
        count = 1
        visited = {loc}
        while p1 != p2:
            p1_neighbors = self._find_neighbor_pipes(graph=graph, loc=p1)
            visited.add(p1)
            p1 = p1_neighbors[0] if p1_neighbors[0] not in visited else p1_neighbors[1]
            p2_neighbors = self._find_neighbor_pipes(graph=graph, loc=p2)
            visited.add(p2)
            p2 = p2_neighbors[0] if p2_neighbors[0] not in visited else p2_neighbors[1]
            count += 1
        visited.add(p1)
        return loc, visited, graph
    
    def part02(self, fname: str) -> int:
        loc, visited, graph = self.part01(fname=fname)
        inside_count = 0
        for r,line in enumerate(graph):
            for c,_ in enumerate(line):
                if (r,c) in visited:
                    continue
                crosses = 0
                x,y = r,c
                while x < len(graph) and y < len(graph[0]):
                    ch = graph[x][y]
                    if (x,y) in visited and ch != 'L' and ch != '7':
                        crosses += 1
                    x += 1
                    y += 1
                if crosses % 2 == 1:
                    inside_count += 1
        return inside_count

if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))