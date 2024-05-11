## General Information
Name: Alex Daniel
Date: May 11, 2024

### To Run
- python failedAttempt.py

### Results


### Description
The algorithm efficiently uses binary search to find the kth smallest prime fraction by iteratively narrowing down the search space based on the number of fractions smaller than or equal to a given mid-point m.

### LeetCode Description
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].