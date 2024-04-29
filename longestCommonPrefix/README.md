## General Information
Name: Alex Daniel
Date: April 29, 2024

### To Run
- python longestCommonPrefix.py

### Results
Speed: 14 ms and beats 78.19% of users
Memory: 11.90 MB and beats 64.67% of users
Time: O(n * m) where n is the number of words and m is the length of the shortest string

### Description
First, check two special cases: one where there's only one word in the array, and the other where the first word is an empty string. In these cases, return the first word. Then, identify the word with the shortest length and iterate for that number of times. In this loop, create a nested loop that iterates through all the words in the array and checks if each character matches the corresponding character in the first word. If they all match, add the character to a string, which is then returned at the end.

### LeetCode Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Topics
- String
- Trie