## General Information
Name: Alex Daniel
Date: May 16, 2024

### To Run
- python evaluateTree.py 

### Results
Speed: 27 ms and beats 94.17% of users
Memory: 12.37 MB and beats 77.67% of users

### Description
Employs Depth-First Search to navigate through each node in the tree, utilizing recursion for backtracking and ultimately delivering the outcome of the entire binary tree evaluation

### Notes
- "and" and & are different. "and" functions as the logical AND operator, while & functions as a bitwise AND operator, which can lead to issues in situations like this problem
- 

### LeetCode Description
You are given the root of a full binary tree with the following properties:

    Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
    Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

The evaluation of a node is as follows:

    If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
    Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

## Topics
- Tree
- Depth-First Search
- Binary Tree
