## General Information
Name: Alex Daniel
Date: March 20, 2024

### To Run
- python mergeInBetween.py

### Results
Speed: 296 ms and beats 100.00% of users
Memory: 22.64 MB and beats 90.72% of users

### Description
I traverse list 1 until I find the insertion point for list 2, marking this node as head. Then, I continue until reaching the end of the segment to keep from list 1, marking this as tail. Next, I connect list 2 at head and link the remaining part of list 1 to the merged list

## Notes
- The manipulation on the variable i is wonky, but functional

### LeetCode Description
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# Topics
- Linked List