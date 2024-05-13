## General Information
Name: Alex Daniel
Date: May 13, 2024

### To Run
- python threeSumClosest.py

### Results
Speed: 469 ms and beats 68.11% of users
Memory: 11.63 MB and beats 69.39% of users

### Description
First, sort the array, as is typically done in sliding window problems. Then, initiate a loop to assign an index to every position in the array except the last two. These positions are reserved for the left and right sliding windows, so we avoid assigning indexes to the same numbers. Within this loop, implement a nested loop using a greedy algorithm to approach the closest sum.

During each iteration, if the current sum is less than the target sum, increase the left pointer to shift to a larger value. Conversely, if the sum exceeds the target, move the right pointer to decrease the total sum. Additionally, within each loop iteration, check if the sum equals the target to expedite the algorithm's termination or if the current sum is closer to the target than previous sums, in which case update the answer.

### LeetCode Description
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Topics
- Array
- Two Pointers
- Sorting