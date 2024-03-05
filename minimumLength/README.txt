## General Information
Name: Alex Daniel
Date: March 5, 2024

### To Run
- python removeNthFromEnd.py

### Results
Speed: 57ms and beats 100.00% of users
Memory: 13.10 MB and beats 66.67% of users

### Description
Check for a special case where the string has only one character. Set the indices for the start and end of the string. Then, iterate through the string while checking if the characters at the current start and end indices match. If they do, increment the start index and decrement the end index, moving towards the center of the string, until the characters no longer match the initial character at the start index. Ensure that the start and end indices do not go past each other. Repeat this process until the prefixes and suffixes no longer match.

### LeetCode Description
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

    Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero times).