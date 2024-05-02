## General Information
Name: Alex Daniel
Date: May 2, 2024

### To Run
- python findMaxK.py

### Results
Speed: 81 ms and beats 97.08% of users
Memory: 11.61 MB and beats 96.49% of users
Time: O(nlog(n)) + O(n) Sort the array and then iterate through the array

### Description
Sort the array first, then set two pointers at both ends. While iterating through the array, if the left pointer becomes larger than zero, it's impossible to find a solution by considering more positive numbers; thus, we return -1. Similarly, if the right pointer becomes a negative value, we exit with -1. This optimization is crucial for efficiency, especially with a large number of negative or positive values. If the absolute value of the left pointer equals the right pointer, we've found the solution. Otherwise, if the absolute value of the left pointer is greater, we increment the left pointer to decrease its value. Vice versa, if the right pointer's absolute value is greater, we decrement it to reduce its value.

### LeetCode Description
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

### Topics
- Array
- Hash Table
- Two Pointers
- Sorting