## General Information
Name: Alex Daniel
Date: February 6, 2024

### To Run
- python uniqueCharacter.py

### Results
Speed: 91ms and beats 70.99% of users
Memory: 11.95 MB and beats 85.92% of users

### Description
First, run through the string and get the character count. Then create a for loop to receive the
characters with a count of one in the character count. Finally, run through the string again and check
if the character has a count of one.

### Notes
- Very similar problem to groupAnagrams
- enumerate() is a built-in function that returns pairs of indices and corresponding elements
- Multiple variables go in a for statement if there are multiple values to deal with
- Ex. a dictionary needs key and a value in the for loop
- Ex. enumerate needs the index and then the element (for index, char in enumerate(s))

### LeetCode Description
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
