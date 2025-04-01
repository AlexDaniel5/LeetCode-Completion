## General Information
Name: Alex Daniel

Date: March 31, 2025

### To Run
- python n-queens.py

### Results
Speed: 10 ms and beats 94.94% of users

Memory: 12.52 MB and beats 75.00% of users

### Description
This program solves the N-Queens problem using backtracking by placing one queen per row while ensuring no two queens threaten each other. It tracks occupied columns, positive diagonals (r + c), and negative diagonals (r - c) using sets for efficient conflict detection. The function backtrack(r) attempts to place a queen in row r, iterating through each column c to find a safe position. If a conflict exists, it skips that column; otherwise, it places the queen, updates the tracking sets, and recursively moves to the next row. If all n queens are placed successfully, the board configuration is saved. If a placement leads to an invalid state, it backtracks by removing the queen and trying the next possible column. This continues until all valid solutions are found. The program efficiently prunes unnecessary searches using sets, reducing the time complexity to approximately O(n!). The final result is a list of all possible board configurations, each represented as a list of strings where "Q" marks queen placements.

### LeetCode Description
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
### Topics
- Array
- Backtracking