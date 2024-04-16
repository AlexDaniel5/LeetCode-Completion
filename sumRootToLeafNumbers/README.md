## General Information
Name: Alex Daniel
Date: April 15, 2024

### To Run
- python sumNumbers.py

### Results
Speed: 10 ms and beats 87.12% of users
Memory: 11.59 MB and beats 85.81% of users

### Description
Traverse the binary tree using Depth-First Search and recursion. During each recursive call to the DFS function, multiply the current sum by 10. This step ensures that each subsequent number added to the sum occupies its own digit position. At each iteration, check if the current node is a leaf node; if it is, return the sum. Otherwise, continue the DFS process by recursively calling the function with the updated sum and the child nodes. The function backtracks at the end, summing up all intermediate sums, and returns the final result.

### LeetCode Description
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

# Topics
- Tree
- Depth-First Search
- Binary Tree