## General Information
Name: Alex Daniel
Date: May 14, 2024

### To Run
- python getMaximumGold.py

### Results
Speed: 4954 ms and beats 17.54% of users
Memory: 11.62 MB and beats 50.88% of users

### Description
Traverse the entire grid using a Depth-First Search approach initiated from each cell. During the DFS, validate if the cell is within bounds and contains gold. Temporarily mark the cell as visited by setting its value to 0 within the ongoing search. Then, explore all feasible paths in the DFS, which recursively backtracks to calculate the maximum gold that can be gathered starting from the specified cell. Upon completion, restore the grid's original values to prepare for subsequent DFS searches from other cells.

### LeetCode Description
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position, you can walk one step to the left, right, up, or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.


### Topics
- Array
- Matrix
- Backtracking