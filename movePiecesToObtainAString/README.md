## General Information
Name: Alex Daniel

Date: Dcemeber 6, 2024

### To Run
- python canChange.py

### Results
Speed: 231 ms and beats 52.18% of users
Memory: 12.95 MB and beats 70.64% of users

### Description
The underscores in the strings are irrelevant, and only the order of the letters matters. While checking the letter order, three conditions need to be validated. First, the letters must appear in the same order. Second, if a matching 'L' character is found, it must be in the same position or to the left of its position in the target string, since 'L' can only move left. Third, if a matching 'R' character is found, it must be in the same position or farther to the right in the target string, as 'R' can only move right. If any of these conditions are not met, the function returns False. Afterward, the function checks for any remaining characters in either string. If there are extra characters that cannot be matched in the other string, the function returns False. If all conditions are satisfied, the function returns True.

### LeetCode Description
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

### Topics
- Two Pointers
- String