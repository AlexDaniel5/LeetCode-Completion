## General Information
Name: Alex Daniel
Date: March 14, 2024

### To Run
- python numSubarraysWithSum.py

### Results
Speed: 225 ms and beats 20.21% of users
Memory: 12.50 MB and beats 94.00% of users

### Description
The code uses the sliding window technique to efficiently count the number of subarrays whose sum is at most equal to a given goal. It then calculates the number of subarrays with a sum exactly equal to the goal by subtracting the counts of subarrays with a sum less than the goal from the counts of subarrays with a sum at most equal to the goal.

## Notes
- This approach is less efficient for solving the problem; I was primarily curious about mastering the sliding window technique rather than relying on hash tables.

### LeetCode Description
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

# Topics
- Array
- Hash table
- Sliding window
- Prefix sum