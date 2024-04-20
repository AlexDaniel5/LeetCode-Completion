## General Information
Name: Alex Daniel
Date: April 20, 2024

### To Run
- python findFarmLand.py 

### Results
Speed: 4953 ms and beats 9.09% of users
Memory: 24.32 MB and beats 90.91% of users

### Description
Iterate through each tile on the grid, and for each tile, verify if it's a farmland tile. Since we're iterating from the top left to the bottom right of the grid, the farmland tile must be the top-left tile of the rectangle if we find one in this iteration. To determine the bottom-right corner of the farmland, employ a DFS search moving continuously downwards and to the right until there's no more farmland. With the top-left and bottom-right indexes identified, convert the farmland into forested land to prevent it from being counted as a separate farmland group later. Repeating this algorithm will eventually yield the solution.

### LeetCode Description
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

## Topics
- Array
- Depth-First Search
- Breadth-First Search
- Matrix
