## General Information
Name: Alex Daniel
Date: March 24, 2024

### To Run
- python findDuplicate.py 

### Results
Speed: 476 ms and beats 67.32% of users
Memory: 23.40 MB and beats 87.33% of users

### Slow Results
Speed: 540 ms and beats 20.86% of users
Memory: 39.58 MB and beats 5.04% of users

### Description
Upon realizing that my initial solution was slower compared to the average, I investigated a more efficient approach that might not be immediately intuitive. The algorithm employs Floyd's Tortoise and Hare algorithm to detect cycles in a sequence. In this context, finding a cycle directly leads to identifying the duplicate number. This is because each number in the sequence points to another index within the list, given the numbers range from 1 to n. Once the slower pointer (Tortoise) gets trapped in the cycle, we initiate another loop to pinpoint the duplicate number and return it as the result.

### Description of Slow Route
Brute force solution involves tallying the occurrences of each integer and recording them in a hash table. Subsequently, it involves traversing the hash table to identify and return the first key associated with a value greater than one.

### LeetCode Description
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

## Topics
- Array
- Two Pointers
- Binary search
- Bit manipulation
