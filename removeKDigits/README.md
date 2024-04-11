## General Information
Name: Alex Daniel
Date: APril 10, 2024

### To Run
- python removeKDigits.py

### Results
Speed: 35 ms and beats 89.26% of users
Memory: 13.11 MB and beats 82.96% of users

### Description
We iterate through each digit in the number. For each digit, we add it to the stack and check if it's greater than the previous digit. If it is, we remove the previous digit from the stack. We repeat this process for every digit in the number. After the loop finishes, if k is still greater than 0, it means the last digits are in increasing order, so we simply remove the last k digits from the stack. Finally, we convert the stack back to a string and remove any preceding zeros after the first non-zero digit. We also ensure that the resulting string isn't empty, as there are special cases to be aware of.
 
### LeetCode Description
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Topics
- String
- Stack
- Greedy
- Monotonic Stack