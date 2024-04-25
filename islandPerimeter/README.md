## General Information
Name: Alex Daniel
Date: April 24, 2024

### To Run
- python islandPerimeter.py

### Results
Speed: 493 ms and beats 11.99% of users
Memory: 12.83 MB and beats 15.55% of users

### Description
Iterate through the grid to find a land tile. Once discovered, ensure it's connected to all other land tiles, then return after the BFS function completes. Track visited tiles without converting them to water, which would inflate the perimeter count. Assess possible movement directions from each land tile: add neighboring land tiles to the queue, and increment the island perimeter for water or out-of-bounds conditions.

## Notes
- Defintely faster routes not using BFS but instead using DFS or neither search algorithms. However, this solution felt unique.

### LeetCode Description
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## Topics
- Array
- Depth-First Search
- Breadth-First Search
- Matrix