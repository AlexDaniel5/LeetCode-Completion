## General Information
Name: Alex Daniel

Date: November 5, 2024

### To Run
- python minChanges.py

### Results
Speed: 19 ms and beats 100.00% of users
Memory: 13.61 MB and beats 41.18% of users

### Description
When partitioning the string, it can always be divided into pairs of two since the string is guaranteed to have an even length. This allows us to iterate over every other character in the string and check if it matches the following character. If a pair doesn't match, a change would be required to achieve matching pairs. Overall, it's a straightforward approach once understood.

### LeetCode Description
You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

    Each substring has an even length.
    Each substring contains only 1's or only 0's.

You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.

### Topics
- String