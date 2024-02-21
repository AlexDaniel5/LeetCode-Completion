## General Information
Name: Alex Daniel
Date: February 21, 2024

### To Run
- python rangeBitwiseAnd.py

### Results
Speed: 38ms and beats 61.54% of users
Memory: 11.62 MB and beats 71.01% of users

### Description
Identify the point where the binary representations of the two arguments share a sequence of ones from the leftmost bit to the right. Use a count variable to track the position of the rightmost shared one. Return the value formed by the shared ones, multiplied by 2 raised to the power of the count (equivalent to using the left shift operator).
The fundamental concept is that when two numbers have common leftmost bits in their binary representation, the smaller number doesn't need to alter those bits to match the larger number.

## Failed Attempt
nitially, I thought comparing the difference between two numbers to the binary digits of 2^(32)-1 could identify shared digits, but a for loop was needed to avoid counting digits larger than the input numbers. To solve this a common prefix MSB was required and resolved in a simpler solution.

### LeetCode Description
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
