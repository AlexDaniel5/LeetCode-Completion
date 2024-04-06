## General Information
Name: Alex Daniel
Date: April 5, 2024

### To Run
- python makeGood.py

### Results
Speed: 11 ms and beats 90.52% of users
Memory: 11.75 MB and beats 29.38% of users

### Description
Iterate through the string, adding characters to a stack. Check if characters are equal without case sensitivity, popping from the stack if they are; then convert the stack back to a string and return it

### Notes
- Checking just the next character in the string isn't sufficient, as removing characters that result in adjacent uppercase and lowercase letters could still leave undesirable adjacent pairs.

### LeetCode Description
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

### Topics
- String
- Stack