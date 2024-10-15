## General Information
Name: Alex Daniel

Date: April 6, 2024

### To Run
- python minRemoveToMakeValid.py

### Results
Speed: 67 ms and beats 89.96% of users
Memory: 14.02 MB and beats 74.90% of users

### Description
Iterate through the string and append the index of every opening parenthesis to a stack. Add every character to the result string in this iteration except closing parentheses when the stack is empty. Also, whenever we encounter a closing parenthesis, pop the index of a corresponding opening parenthesis from the stack so it won't be removed in the final step. In the final step, iterate through our stack of indexes and set all indexes within the result string to nothing, thus removing all opening parentheses that didn't have a matching closing parenthesis.

### LeetCode Description
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.


 ### Topics
 - String
 - Stack