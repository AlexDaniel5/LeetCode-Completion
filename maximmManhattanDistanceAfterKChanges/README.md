## General Information
Name: Alex Daniel

Date: June 19, 2025

### To Run
- python maxDistance.py

### Results
Speed: 6120 ms and beats 10.00% of users
Memory: 12.89 MB and beats 100.00% of users
Complexity: O(N)

### Description
The key part of this solution is the count function. Essentially, each time we flip a direction, it increases the total distance by two because flipping converts one step from the opposite direction into the dominant direction, effectively adding two to the net distance.

At every iteration, we calculate the maximum number of flips we can perform to maximize this distance. Besides that, we add the remaining unflipped movements in both the horizontal and vertical directions to get the total possible distance traveled.

### LeetCode Description
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

    'N' : Move north by 1 unit.
    'S' : Move south by 1 unit.
    'E' : Move east by 1 unit.
    'W' : Move west by 1 unit.

Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|. 

### Topics
- Hash Table
- Math
- String
- Counting