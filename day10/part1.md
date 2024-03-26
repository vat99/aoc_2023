## Goal

Find the point that is furthest from the start of the graph from either direction (guaranteed to be 2).

## High Level Approach

Convert the input to a graph. Use to pointers that move in lock step along opposite directions of the graph until they coincide. Return the number of steps.

1. Read in the files as normal.

2. Record the location of the 'S' symbol as coordinates.

3. Continue reading the rest of the input, should end up with a `List[str]`.

4. Create two pointers both starting at 'S'. Look at all 4 neighbors of 'S' and find the 2 adjacent neighbors.

5. While the pointers are not on the same space, advance pointers along correct direction and iterate count.

## Helper Functions

Given a location in the grid, find matching side that isn't already visited.

## Edge Cases

None that I can see right now.
