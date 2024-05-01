## General Information
Name: Alex Daniel
Date: May 1, 2024

### To Run
- python reversePrefix.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 11.70 MB and beats 66.57% of users

### Description
Given a word and a character ch, this function locates the index of the first occurrence of ch in the word. If the character is not found, it returns the original word. Otherwise, it reverses the prefix of the word up to and including ch, and then concatenates this reversed prefix with the remaining part of the word, and returns the result.

### LeetCode Description
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

# Topics
- String
- Two Pointers