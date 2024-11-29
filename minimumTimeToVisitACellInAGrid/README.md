## General Information
Name: Alex Daniel

Date: November 29, 2024

### To Run
- python minimumTime.py

### Results
Speed: 2988 ms and beats 28.57% of users
Memory: 35.37 MB and beats 71.43% of users

### Description
First, check if the initial move is possible by ensuring that the time in the neighboring cells is either 1 or 0. After the first move, all subsequent moves are allowed, as you can move back and forth between visited cells. To find the most efficient way to reach the end, we use a heap priority queue instead of BFS, as we need to determine the least costly path rather than just any path.

When moving to a new cell, we must calculate the resulting time. This can either be the current time plus one (for a direct move) or one greater than the cell’s value (if revisiting a cell to reach a new one). We need to ensure that the time increases in steps of two. For example, if time = 1 and gridValue = 4, we would need to move back and forth to increase the time to 3, and then again to 5, since we are incrementing time by 2. If time = 2 initially, no such adjustment is needed, as it would already be aligned with the grid value.

### LeetCode Description
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

### Topics
- Array
- Breadth-First Search
- Graph
- Heap (Priority Queue)
- Matrix
- Shortest Path