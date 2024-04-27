## General Information
Name: Alex Daniel
Date: April 26, 2024

### To Run
- python isMatch.py

### Results
Speed: 16 ms and beats 94.77% of users
Memory: 12.14 MB and beats 7.93% of users

### Description
We establish the possibility that the pattern p might include a wildcard match of an asterisk that could affect whether the string s fits the pattern, thus we use a cache to include the possibility of including certain characters or skipping them, such as an asterisk. Also, the cache helps prevent revisiting already processed combinations, reducing computational overhead. Then, we recursively explore all possible matches between s and p, taking into account wildcard characters and updating the cache as we progress. Finally, based on the computed results, the algorithm returns True if there is a valid match, and False otherwise, optimizing the matching process through efficient memoization techniques.

### LeetCode Description
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

### Topics
- String
- Dynamic Programming
- Recursion