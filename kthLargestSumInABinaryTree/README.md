## General Information
Name: Alex Daniel
Date: October 21, 2024

### To Run
- python kthLargestLevelSum.py

### Results
Speed: 92 ms and beats 100.00% of users
Memory: 91.71 MB and beats 43.75% of users

### Description
Use BFS to determine the sum of each level. The length of the queue indicates how many nodes exist in the current level. During each iteration, nodes from the next level are added to the queue, and the value of each node is added to the sum. Add all sums to a list, sort it after traversing the tree, and return the k-th largest number from the sorted list

## Notes
- Could improve memory usage by using a hashmap to remove the smallest level sum once more than k values are stored

### LeetCode Description
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

### Topics
- Tree
- Breadth-First Search
- Sorting
- Binary Tree