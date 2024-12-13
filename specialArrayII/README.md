## General Information
Name: Alex Daniel

Date: December 13, 2024

### To Run
- python isArraySpecial.py

### Results
Speed: 69 ms and beats 29.64% of users
Memory: 43.24 MB and beats 60.83% of users

### Description
First, iterate through the list and check if the difference between adjacent numbers has alternating parity. For each passing check, increment a counter and append it to a list. In the next loop, verify if the count consistently increases within the index range to determine if the range maintains parity.

### LeetCode Description
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that
subarray
nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

# Topics
- Array
- Binary Search
- Prefix Sum