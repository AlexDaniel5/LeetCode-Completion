Name: Alex Daniel
Date: October 1, 2023

To Run:
- make
- ./romanToInt

Description:
Iterates through every character in the string. Checks if the value of the characters to its right
are larger or smaller deciding if it should add or subtract the current value of the character to
the total.

LeetCode Description:
Roman numerals are usually written largest to smallest from left to right. However, the numeral
for four is not IIII. Instead, the number four is written as IV. Because the one is before the
five we subtract it making four. The same principle applies to the number nine, which is written
as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.