## General Information
Name: Alex Daniel
Date: February 13, 2024

### To Run
- python elementsBySign.py

### Results
Speed: 1110ms and beats 93.87% of users
Memory: 44.68 MB and beats 62.25% of users

### Description
The program organizes the answer array by iterating through the input array and placing positive numbers at even indices while assigning negative numbers
to odd indices. It utilizes separate index pointers for positive and negative numbers to ensure a well-organized rearrangement.

### Notes
- Arrays need to have their indices set if we want to assign values at specific positions.

### LeetCode Description
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.