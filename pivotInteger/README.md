## General Information
Name: Alex Daniel
Date: March 13, 2024

### To Run
- python pivotInteger.py

### Results
Speed: 15 ms and beats 84.42% of users
Memory: 11.62 MB and beats 54.55% of users

### Description
First, calculate the total sum of n and designate it as the right sum. Then, iterate from 1 to n, incrementally adding each number to the left sum. Ensure to subtract the current number from the right sum after verifying if it equals the left sum, as the pivot integer is encompassed by both sums.

### LeetCode Description
Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Topics
- Math
- Prefix sum