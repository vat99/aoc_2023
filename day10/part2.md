## Goal

Find the number of inside points that are fenced in by the pipe maze.

## High Level Approach

Credits to this [solution](https://github.com/OskarSigvardsson/adventofcode/blob/master/2023/day10/day10.py) also from the [subreddit](https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/khtkdg9/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 

### Approach 1

1. Perform part1 and save all pipes that form the maze.
2. For every point not in the maze just extend in a straight line towards the bottom of the graph, count the number of times it crosses the maze to determine if it is inside or not. (odd times -> inside, even times -> outside)

Note if a ray goes along an edge that is parallel to it just count it as 0. 

### Approach 2

Take same approach as #1 but do a flood fill for some number of points to hopefully speed up the process?
