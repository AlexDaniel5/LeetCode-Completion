## General Information
Name: Alex Daniel
Date: March 29, 2024

### To Run
- python countSubarrays.py 

### Results
Speed: 993 ms and beats 26.67% of users
Memory: 23.40 MB and beats 60.00% of users

### Description
First, the code utilizes Python's max function to determine the maximum element within the array. Subsequently, it traverses through the array, incrementing a count each time it encounters an element that matches the maximum value. When this count reaches k or exceeds it, the code adjusts the left end of the window, iterating until it surpasses another occurrence of the maximum element. This adjustment is crucial as it allows the algorithm to account for all subarrays to the left of the window, considering them as potential candidates since their elements do not influence the count of maximum elements within the subarray.

### LeetCode Description
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

## Topics
- Array
- Sliding Window
