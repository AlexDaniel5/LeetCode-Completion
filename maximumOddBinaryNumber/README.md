## General Information
Name: Alex Daniel
Date: March 1, 2024

### To Run
- python maximumOddBinaryNumber.py

### Results
Speed: 16ms and beats 70.07% of users
Memory: 11.61 MB and beats 72.26% of users

### Description
Determine the count of digits and occurrences of 1 in the binary number. Generate a string consisting of all 0s to serve as the output representation. In a specific scenario where there are no 1s in the binary number, promptly return. Otherwise, transform the string into a list for convenient manipulation, set the last digit to 1, and set all higher-order digits to 1 for the count of 1s in the original input number. Subsequently, convert the list back into a string and return the modified representation.

### LeetCode Description
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.