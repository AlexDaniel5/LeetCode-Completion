## General Information
Name: Alex Daniel
Date: Feburary 5, 2024

### To Run
- python groupAnagrams.py

### Results
Speed: 84ms and beats 29.66% of users
Memory: 21.32 MB and beats 5.26% of users

### Description
First, determine if the integer is negative to facilitate the reversal process, and store a boolean flag indicating the negativity.
Remove the negative sign to expedite string manipulation. Convert the integer to a string, reverse the string, and convert it back to
an integer. Reapply the negative sign if the original integer was negative. Finally, validate if the signed integer falls within its
32-bit constraint.


### Notes
Hashable is when an object:
- Has a numerical value computed based on its contents
- Can't be changed after creation
We convert a dictionary into a tuple so we can compare it to other dictionaries in this program.

### LeetCode Description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
