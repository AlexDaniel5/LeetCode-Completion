## General Information
Name: Alex Daniel
Date: April 19, 2024

### To Run
- python numIslands.py

### Results
Speed: 210 ms and beats 79.58% of users
Memory: 26.97 MB and beats 79.88% of users

### Description
Check each tile in the grid to determine if it's land. If it is, mark it as water to prevent counting the same island multiple times. Use breadth-first search to achieve this efficiently: begin with a land tile, mark it as water, and add it to the queue. Then, explore adjacent tiles in all cardinal directions. If a tile is land, add it to the queue and mark it as water. Repeat this process iteratively and increment a counter each time a BFS search is completed. This approach will effectively convert all land tiles into water and accurately count the islands.

### LeetCode Description
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Topics
- Array
- Depth-First Search
- Breadth-First Search
- Union Find
- Matrix