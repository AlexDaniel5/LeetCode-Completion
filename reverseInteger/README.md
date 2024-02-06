## General Information
Name: Alex Daniel
Date: January 29, 2024

### To Run
- python reverseInteger.py

### Results
Speed: 19ms and beats 57.12% of users
Memory: 11.65 MB and beats 90.79% of users

### Description
First, determine if the integer is negative to facilitate the reversal process, and store a boolean flag indicating the negativity.
Remove the negative sign to expedite string manipulation. Convert the integer to a string, reverse the string, and convert it back to
an integer. Reapply the negative sign if the original integer was negative. Finally, validate if the signed integer falls within its
32-bit constraint.

### Notes
I initially tested the code utilizing the math module to check if the integer was within 32 bits, which is a slow approach and decided
to change the program without using exponents. Upon submitting it to LeetCode, the first time it performed faster with a 90.85% speed.
Consequently, I reverted to my original answer, which doesn't involve string manipulation and showed to be even faster in the past. 
Surprisingly, this change resulted in a 1.5x drop in speed, which went against the original results. The speed measurement on LeetCode
seems to be somewhat inaccurate, and I'll disregard it moving forward.

### LeetCode Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
