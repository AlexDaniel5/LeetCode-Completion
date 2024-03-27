## General Information
Name: Alex Daniel
Date: March 27, 2024

### To Run
- python numSubarrayProductLessThanK.py

### Results
Speed: 512 ms and beats 59.74% of users
Memory: 13.74 MB and beats 84.49% of users

### Description
Iterate through the list, multiplying each integer to calculate a running product. If the product exceeds a value k, shift the left interval of the window to the right. Otherwise, continue multiplying each number and use a clever formula to determine the count of subarrays containing these integers.

### LeetCode Description
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Topics
- Array
- Sliding Window