## General Information
Name: Alex Daniel
Date: April 1, 2024

### To Run
- python isIsomorphic.py

### Results
Speed: 14 ms and beats 96.91% of users
Memory: 12.99 MB and beats 51.61% of users

### Description
Iterate through each character in both strings s and t, mapping each character from s to its corresponding character in t, while keeping track of all the characters we've mapped. During each iteration, check if the current character in s has already been mapped. If it has, verify if it is mapped to the same character in t; if so, continue to the next iteration. If the mapping is to a different character in t, or if a different character in s attempts to map to an already mapped character in t, return False. If the loop completes without returning False, the two strings are isomorphic.

### LeetCode Description
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Topics
- String
- Hash Table