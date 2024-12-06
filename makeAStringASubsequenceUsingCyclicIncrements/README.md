## General Information
Name: Alex Daniel

Date: December 5, 2024

### To Run
- python canMakeSubsequences.py

### Results
Speed: 87 ms and beats 92.31% of users
Memory: 12.81 MB and beats 76.92% of users

### Description
Use a dictionary to map each character to its next character. Initialize two pointers, one for each string. Use a while loop to iterate through both strings, checking if either pointer reaches the end of its respective string. In each iteration, compare the characters at both pointers. If they are the same, or if the character at the first pointer maps to the character at the second pointer, increment the second pointer. The first pointer will always be incremented in each iteration. If the loop ends because the second pointer has reached the end of the second string, return True; otherwise, return False.

## Notes
- We could use ASCII to map characters to the next character, but because of the case z to a, I liked the idea of a dictionary more

### LeetCode Description
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

### Topics
- Two Pointers
- String