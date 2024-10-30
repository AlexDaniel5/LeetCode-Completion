## General Information
Name: Alex Daniel
Date: October 30, 2024

### To Run
- python maxMoves.py

### Results
Speed: 178 ms and beats 100.00% of users
O time: O(3^N), without memo it's O(M * 3^N)
Memory: 37.45 MB and beats 10.00% of users

### Description
First, we need some values to solve this problem: the grid dimensions, an array storing possible moves, and a cache to store results at each cell. We start a DFS search from each cell in the first column. In the DFS, we return immediately if there is already a cached result for the current cell or if we’ve reached the rightmost column. Since we are always maximizing our result, caching is effective here because the path taken to reach each cell doesn’t affect the outcome. Once the DFS completes for each cell in the first column, the maximum number of moves will be determined.

### LeetCode Description
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

    From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.

Return the maximum number of moves that you can perform.

### Topics
- Array
- Dynamic Programming
- Matrix