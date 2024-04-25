## General Information
Name: Alex Daniel
Date: April 25, 2024

### To Run
- python longestIdealString.py

### Results
Speed: 1700 ms and beats 44.44% of users
Memory: 12.97 MB and beats 100.00% of users

### Description
Iterate through the string to determine the numeric value of each character, where a is 0 and z is 25. Use a variable longest that represents the longest subsequent string ending at the current character; this starts as 1 because the first character is always the same as the previous character. Then iterate through the previous characters we've encountered; if they haven't been encountered before, this will be 0. In this iteration, check if the absolute difference between the current character and the previous characters is less than k. If so, update longest to be the maximum of its current value. Afterwards, update the current character to hold the longest subsequence that can be made ending at that character. Finally, once the loop is done, return the longest subsequent character that can be made ending at any of the characters a to z.

### LeetCode Description
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

    t is a subsequence of the string s.
    The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

### Topics
- Hash Table
- String
- Dynamic Programming