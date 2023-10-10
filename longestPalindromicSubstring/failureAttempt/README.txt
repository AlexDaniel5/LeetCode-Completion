Name: Alex Daniel
Date: October 9, 2023

To Run:
-  gcc -std=c99 -Wall failedPalindrome.c -o failedPalindrome
- ./failedPalindrome

Idea:
Have two indexes, one at the leftmost character and the other at the rightmost character of the substring. If the characters match
move in towards the substring. Do this for every possible substring.

Failure Reason:
If the outside of the substring matches but not the inside the program considers it still to be a palindrome. Also, the program runs
slow in general but I didn't have issues with this yet.

Test case failed:
Input:
s = "aacabdkacaa"

Output:
acabdkaca

Expected Output:
aca

LeetCode Description:
Given a string s, return the longest palindromic substring in s.