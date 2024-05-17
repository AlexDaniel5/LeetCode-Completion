## General Information
Name: Alex Daniel
Date: May 17, 2024

### To Run
- python removeLeafNodes.py 

### Results
Speed: 26 ms and beats 92.00% of users
Memory: 12.91 MB and beats 20.00% of users

### Description
The algorithm iteratively removes leaf nodes with a specific target value from a binary tree using a depth-first search approach simulated with a stack. It keeps track of each node's parent using a dictionary to facilitate the removal of leaf nodes by updating the parent's child reference. During traversal, each node is visited, and its children are added to the stack. If a node is identified as a leaf with the target value, it is removed by setting the corresponding child reference in its parent to None.

### LeetCode Description
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

## Topics
- Tree
- Depth-First Search
- Binary Tree
