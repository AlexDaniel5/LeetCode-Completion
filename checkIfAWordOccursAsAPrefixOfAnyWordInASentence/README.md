## General Information
Name: Alex Daniel

Date: Decemeber 2, 2024

### To Run
- python isPrefixOfWord.py
- python basicSolution.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 12.16 MB and beats 6.98% of users

### Description
Solving this problem using Python's built-in methods made it too easy, so I decided to attempt the solution without them. With built-in methods, you can simply split the sentence into words and iterate through each word, tracking the word index and using startswith() to check if the prefix exists.

Without using built-in methods (except for len, which is easy to replicate), we need to iterate through the sentence character by character. We check for spaces to determine word boundaries and identify potential prefixes. When a prefix is detected, we compare the first character with the search word's first letter. If they match, we increment an index that tracks the position within the search word. Each time the index is incremented, we check if it reaches the length of the search word. If a character doesn't match, we reset the index to 0. With i reset to 0, we stop matching until we encounter another space or the index is greater than 0, indicating a new potential prefix.

### LeetCode Description
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

### Topics
- Two Pointers
- String
- String Matching