## General Information
Name: Alex Daniel
Date: May 6, 2024

### To Run
- python removeNodes.py

### Results
Speed: 1008 ms and beats 90.73% of users
Memory: 96.30 MB and beats 79.47% of users
Time: O(n) Due to reversing the linked list twice and iterating through it once

### Description
First, reverse the linked list. Then, iterate through the reversed list in a loop, checking if the next node is larger than or equal to the current node. If it is, keep it in the list; otherwise, remove it. Continue this process until there are no more nodes to check for removal. Finally, reverse the list back to its original order and return the modified linked list.

### LeetCode Description
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

# Topics
- Linked List
- Stack
- Recursion
- Monotonic Stack