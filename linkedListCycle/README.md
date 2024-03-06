## General Information
Name: Alex Daniel
Date: March 6, 2024

### To Run
- python hasCycle.py

### Results
Speed: 30ms and beats 80.76% of users
Memory: 18.52 MB and beats 92.33% of users

### Results (Slow)
Speed: 1857ms and beats 5.02% of users
Memory: 18.80 MB and beats 58.52% of users

### Description
Initialize two pointers at the beginning of the linked list. Assign one pointer to advance two nodes at a time within the cycle, and the other pointer to move forward one node at a time. The rationale behind this approach is that, given a cycle, the faster-moving pointer will eventually either intersect with the slower one or reach the end of the linked list if no cycle exists. This technique is known as Floyd's Cycle Finding Algorithm and proves to be significantly more efficient than storing all node data and repeatedly checking for duplicate entries.

### LeetCode Description
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.