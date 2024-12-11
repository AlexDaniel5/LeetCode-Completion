## General Information
Name: Alex Daniel

Date: Decemeber 11, 2024

### To Run
- python maximumBeauty.py

### Results
Speed: 298 ms and beats 33.33% of users
Memory: 20.10 MB and beats 55.56% of users

### Description
This is a sliding window solution. First, sort the array to simplify finding valid subsequences and eliminate the need for searching. Use two pointers: the left pointer tracks the smallest number in the current window, and the right pointer tracks the largest. Expand the window by moving the right pointer until the difference between the largest and smallest numbers exceeds k * 2. When this happens, adjust the left pointer to shrink the window and ensure it meets the condition.

### LeetCode Description
You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can do the following:

    Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
    Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].

The beauty of the array is the length of the longest subsequence consisting of equal elements.

Return the maximum possible beauty of the array nums after applying the operation any number of times.

Note that you can apply the operation to each index only once.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.

### Topics
- Array
- Binary Search
- Sliding Window
- Sorting