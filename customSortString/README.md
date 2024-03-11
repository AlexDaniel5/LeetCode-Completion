## General Information
Name: Alex Daniel
Date: March 11, 2024

### To Run
- python customSortString.py

### Results
Speed: 6 ms and beats 97.74% of users
Memory: 11.82 MB and beats 21.51% of users

### Description
Calculate the occurrence frequency of each character in string s. Once we have the frequency information, we can organize the characters accordingly and append them to the output string. Consider the output string as a list, facilitating character additions. During the iteration, make sure to remove each character from the hash table to avoid redundant additions in the subsequent loop. In the next iteration, add the remaining characters in any order, as their sequence no longer matters.

### LeetCode Description
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

## Topics
- Hash table
- String
- Sorting
