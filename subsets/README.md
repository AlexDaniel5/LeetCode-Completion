## General Information
Name: Alex Daniel
Date: May 20, 2024

### To Run
- python subsets.py

### Results
Speed: 15 ms and beats 68.54% of users
Memory: 11.67 MB and beats 96.18% of users

### Description
The algorithm functions like a binary tree. It employs a recursive function that makes a decision for each number at index i to either include it in the current subset or skip it, resulting in two recursive calls for each number in the array. When the index counter surpasses the length of the array, it simply returns. This process ensures that all possible subsets are generated and collected in the result, providing the complete answer

### LeetCode Description
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

### Topics
- Array
- Backtracking
- Bit Manipulation
