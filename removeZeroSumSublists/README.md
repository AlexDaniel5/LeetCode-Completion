## General Information
Name: Alex Daniel
Date: March 12, 2024

### To Run
- python removeZeroSumSublists.py

### Results
Speed: 22 ms and beats 62.50% of users
Memory: 12.02 MB and beats 75.00% of users

### Description
First, we add a dummy node to the left of the head to facilitate removal of the head if needed. Then, we traverse the linked list while maintaining a hash map of all the prefix sums encountered up to each node. Next, we iterate through the linked list again. During this pass, we check if there are matching prefix sums within the hash map. If matching prefix sums are found, we skip all nodes in-between them by adjusting the next pointers accordingly. Finally, we return the modified linked list, excluding the dummy node added at the beginning.

### LeetCode Description
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

# Topics
- Hash table
- Linked list