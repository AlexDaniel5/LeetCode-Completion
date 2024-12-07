## General Information
Name: Alex Daniel

Date: Decemeber 4, 2024

### To Run
- python validParantheses.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 12.32 MB and beats 5.58% of users
Time complexity: O(N)

### Description
This solution can be efficiently using a dictionary to match each opening bracket with its corresponding closing bracket. During the loop, when an opening bracket (key) is encountered, it's pushed onto the stack. When a closing bracket is encountered, we check if the stack contains an opening bracket. If it does, we pop the most recent bracket from the stack and check if it matches the closing bracket. If it does, the loop continues; otherwise, it returns False. If the loop finishes, it means all closing brackets are matched, but there may still be unmatched opening brackets left in the stack. We return True if the stack is empty (all brackets are paired), and False if there are unmatched opening brackets remaining.

### LeetCode Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


### Topics
- String
- Stack