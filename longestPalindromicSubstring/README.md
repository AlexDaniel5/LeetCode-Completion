## General Information
Name: Alex Daniel
Date: October 9, 2023

### To Run
- make
- ./longestPalindrome

### Description
For each index of the string check if an even or odd palindrome can be made. In an odd palindrome, the starting index
is the middle of the palindrome. Then go outwards from the middle with two indexes (right and left) and check if the
characters are still matching. In an even palindrome, the characters adjacent in the middle match and we move outwards
from the two middle characters and again check if they match. After both checks we see if it's the new longest palindrome,
if it is, store the index of where the palindrome starts and the length of the palindrome. Thus, we can easily copy the string
at the end of the program.

### LeetCode Description
Given a string s, return the longest palindromic substring in s.
