## General Information
Name: Alex Daniel
Date: May 12, 2024

### To Run
- python largestLocal.py

### Results
Speed: 135 ms and beats 32.18% of users
Memory: 11.89 MB and beats 96.55% of users

### Description
Initialize the result array with all 0s. Then iterate through both the result array and the local grids, identifying the largest integer within each local grid. Overall, a straightforward solution.

### LeetCode Description
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

    maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

### Topics
- Array
- Matrix