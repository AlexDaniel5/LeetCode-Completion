## General Information
Name: Alex Daniel
Date: Dec 10, 2024

### To Run
- python maximumLength.py 

### Results
Speed: 190 ms and beats 21.43% of users
Memory: 12.06 MB and beats 5.88% of users

### Description
This brute-force solution prioritizes checking the largest possible answers first. We start with a substring length two less than the input string's length, as the longest potential answer is a substring of repeated characters. For each substring length, we iterate through the string, slice substrings, and add them to the hashmap if all their characters match. After this loop, we check if the hashmap contains any value of three. If it does, we return the substring length. Otherwise, we decrement the substring length counter, clear the hashmap to optimize memory usage, and repeat. If no valid substring is found, we return -1.

### LeetCode Description
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

## Topics
- Hash table
- String
- Binary search
- Sliding window
- Counting