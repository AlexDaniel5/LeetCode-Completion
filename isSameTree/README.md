## General Information
Name: Alex Daniel
Date: February 26, 2024

### To Run
- python isSameTree.py

### Results
Speed: 13ms and beats 66.70% of users
Memory: 11.75 MB and beats 64.43% of users

### Description
The main program is implemented as a recursive function. It begins by checking if both tree nodes are empty; if so, it returns True. Alternatively, if both tree nodes contain values, it checks if the values are the same. It then recursively calls the same function for the children nodes, ensuring a comprehensive comparison of all nodes in the tree. If neither of these conditions is met, it indicates that one node extends further than the corresponding node in the other tree, leading to a return of False.

### LeetCode Description
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
