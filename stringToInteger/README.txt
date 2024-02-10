## General Information
Name: Alex Daniel
Date: February 10, 2024

### To Run
- python myAtoi.py

### Results
Speed: 7ms and beats 99.41% of users
Memory: 11.57 MB and beats 98.02% of users

### Description
The program converts a given string to a 32-bit signed integer, following specific rules. It handles rare cases, such as an empty
string, by returning 0. It iterates through the characters of the input string, skipping spaces, detecting the sign of the number,
and accumulating digits until a non-digit character is encountered. The result is then adjusted for sign and checked against the
32-bit signed integer range before being returned.

### LeetCode Description
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.
