## General Information
Name: Alex Daniel
Date: April 17, 2024

### To Run
- python smallestFromLeaf.py

### Results
Speed: 19 ms and beats 97.50% of users
Memory: 14.80 MB and beats 75.00% of users

### Description
I use depth-first search to traverse the binary tree. When faced with the choice of exploring either the left subtree or the right subtree, I opt to return the minimum result between the two. In cases where there's only one subtree available, we simply continue iterating through that subtree. During traversal, whenever we encounter a node within the binary tree, I convert the integer value of the node into its corresponding character. This conversion is achieved by adding 97, which is the Unicode code point for the character "a", and then adding the node's value. By continuing this process recursively, we eventually arrive at the desired result.

### Notes
- ord() gets the unicode of a character, using this function is slower than simply writing 97 for "a"
- chr() converts the unicode to a character
- In the context of the provided example from LeetCode, where "a" is represented by 0 and "b" by 1, and so forth, we add 97 (the Unicode code point of "a") to maintain the mapping to alphabetical characters

### LeetCode Description
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

    For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

# Topics
- String
- Tree
- Depth-First Search
- Binary Tree