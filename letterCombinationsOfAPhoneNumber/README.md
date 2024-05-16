## General Information
Name: Alex Daniel
Date: May 15, 2024

### To Run
- python letterCombinations.py

### Results
Speed: 9 ms and beats 86.48% of users
Memory: 11.73 MB and beats 40.10% of users

### Description
First, check if the array is empty. If it is, return an empty array. Otherwise, call a recursive function. Within the recursive function, check if the digits array is empty. If it is, add whatever remains of combo and return from the function; the base case. Otherwise, for every letter that matches the first letter of digits, call the recursive function again with the variable combo appended with the letter matching the digit and the rest of digits without the first digit. This recursive function will repeat until it generates the entire output.

### LeetCode Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Topics
- Hash Table
- String
- Backtracking