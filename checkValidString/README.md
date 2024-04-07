## General Information
Name: Alex Daniel
Date: April 7, 2024

### To Run
- python checkValidString.py 

### Results
Speed: 7 ms and beats 96.10% of users
Memory: 11.80 MB and beats 25.54% of users

### Description
Iterate through the string with two variables representing possible counts: pMax, assuming all asterisks are opening brackets, and pMin, assuming all asterisks are closing parentheses. If pMax becomes negative, it indicates an excess of closing brackets, likely near the string's start, making it invalid. If pMin goes negative, it suggests an incorrect treatment of brackets with the asterisks, necessitating a change in perspective. A final pMin value of 0 denotes a valid string.

### LeetCode Description
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


## Topics
- String
- Stack
- Dynamic Programming
- Greedy
