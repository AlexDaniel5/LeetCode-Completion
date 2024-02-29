## General Information
Name: Alex Daniel
Date: February 29, 2024

### To Run
- python isEvenOddTree.py

### Results
Speed: 425ms and beats 86.05% of users
Memory: 66.10 MB and beats 39.53% of users

### Description
Initialize a queue with the root and set the level to zero. Then, create a loop to iterate through each level. Inside this loop, reset the previous node variable and determine the number of elements on the current level using the queue. This count will determine the number of iterations for the nested loop.
In the nested loop, pop a node from the left of the queue and check if the popped node satisfies the level conditions. After processing the node, add its children to the queue for the next iteration of the outer loop. If all nodes pass the conditions without any breaking, return True

### LeetCode Description
A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.