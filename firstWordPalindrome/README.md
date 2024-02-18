## General Information
Name: Alex Daniel
Date: February 16, 2024

### To Run
- python firstPalindrome.py

### Results
Speed: 69ms and beats 24.44% of users
Memory: 11.79 MB and beats 95.10% of users

### Description
For each word, find the middle of the word. Check if the first character matches the last character until reaching
the middle. If this condition is met, return the word.

## Notes
- Rounding down during division works perfectly in this scenario, as we don't need to check the character in the middle
if the number of characters is odd.
- When i is 0, using -i gives 0, so we need to add one to check the actual last character at position -1.

### LeetCode Description
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.