## General Information
Name: Alex Daniel
Date: February 3, 2024

### To Run
- python maxDistanceArray.py

### Description
First, sort the array. Then divide the array into subarrays with three elements each; my failure attempt explains how this is done.
Finally, check in each subarray if all the elements are no more different than k, if they are return an empty array.

### Notes
I initially thought it would be a good idea to implement a quicksort function. However, my attempt didn't work as expected. Instead,
I found a simpler solution by using the built-in sort function, which turned out to be effective in resolving the issues I encountered.

### LeetCode Description
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

    Each element of nums should be in exactly one array.
    The difference between any two elements in one array is less than or equal to k.

Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
