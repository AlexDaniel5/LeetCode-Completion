## General Information
Name: Alex Daniel

Date: December 16, 2024

### To Run
- python getFinalState.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 12.30 MB and beats 7.79% of users
Time Complexity: O(N∗Log(N)+K∗Log(N))

### Description
Use a min-heap to maintain a sorted version of the list, prioritizing the elements' values and breaking ties using their indices. Whenever an element in the heap is multiplied, ensure the corresponding change is reflected in the original list as well.

### LeetCode Description
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

    Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
    Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.

# Topics
- Array
- Math
- Heap (Priority Queue)
- Simulation