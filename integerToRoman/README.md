## General Information
Name: Alex Daniel
Date: April 27, 2024

### To Run
- python intToRoman.py

### Results
Speed: 15 ms and beats 98.86% of users
Memory: 11.55 MB and beats 77.30% of users
Time: O(n) where n is the number of symbols in the symbol list

### Alternate Solution Results
Speed: 19 ms and beats 95.27% of users
Memory: 11.70 MB and beats 41.11% of users

### Alternate Solution Description
In my exploration, I employed multiple if statements to mimic the behavior of the original solution, aiming to grasp their differences. What I found is that utilizing a symbol list is significantly more memory-efficient compared to using numerous if statements. This efficiency stems from the reduced space the code occupies. Moreover, this approach is slightly faster due to a reduction in branching, enhancing its overall performance.

### Description
We utilize a symbol list that maps every possible value as shown in the notes. Then, we iterate through this symbol list, checking if the current number is greater than or equal to the value associated with the symbol we're examining in the loop. If this condition is met, we add the symbol to our result string a number of times equal to the integer division of the number by the value. Additionally, we subtract this value from the number using the modulo operation, conveniently performed within the loop.

### Notes
- The table given is missing some values, here's the corrected version:
Symbol       Value
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000

### LeetCode Description
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

## Topics
- Hash Table
- Math
- String