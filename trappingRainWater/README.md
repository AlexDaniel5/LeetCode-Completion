## General Information
Name: Alex Daniel
Date: April 12, 2024

### To Run
- python trap.py

### Results
Speed: 75 ms and beats 89.15% of users
Memory: 13.18 MB and beats 87.48% of users

### Description
First, iterate through the array in reverse to determine the highest height on the right end. Then, iterate through the array again to determine the highest height on the left end. While iterating through the array, compare the minimum of the left and right heights for each column. This minimum value represents how high the water level would be at that column. Subtract this minimum value from the height of the column; only positive differences indicate areas where water can accumulate. Accumulate these positive differences in an integer variable throughout the loop. Finally, return the accumulated value, which represents the total trapped water.

### LeetCode Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Topics
- Array
- Two pointers
- Dynamic Programming
- Stack
- Monotonic Stack