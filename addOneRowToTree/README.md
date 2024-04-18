## General Information
Name: Alex Daniel
Date: April 16, 2024

### To Run
- python addOneRow.py

### Results
Speed: 26 ms and beats 94.55% of users
Memory: 15.96 MB and beats 18.18% of users

### Description
First, the code checks if the task is to add a row immediately, indicating that there's only one child node and the new row must be added to its left side. Then, it invokes a recursive function that traverses the binary tree in a layered manner, keeping track of the current layer. When the function reaches the layer just before the new row is added, it creates new nodes for the row and attaches the existing subtrees to these new nodes. Finally, the updated root node is returned.

### LeetCode Description
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

## Topics
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree