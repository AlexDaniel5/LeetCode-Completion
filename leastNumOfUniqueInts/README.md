## General Information
Name: Alex Daniel
Date: February 15, 2024

### To Run
- python leastNumOfUniqueInts.py

### Results
Speed: 601ms and beats 19.84% of users
Memory: 37.81 MB and beats 28.10% of users

### Description
Initially, we obtain a count of all unique numbers in the input array and arrange the list by their respective counts.
Subsequently, we iterate through the sorted list, disregarding the first k integers, and determine uniqueness by
ensuring each integer has not been encountered before.

## Notes
- I rushed the answer, I wanted to go out tonight.
- The sort command in the program checks for tiebreakers to ensures a stable sort, preserving the relative order of elements with equal counts in the original list during the sorting process.

### LeetCode Description
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
