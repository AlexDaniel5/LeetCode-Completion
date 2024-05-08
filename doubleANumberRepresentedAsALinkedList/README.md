## General Information
Name: Alex Daniel
Date: May 7, 2024

### To Run
- python doubleIt.py 

### Results
Speed: 426 ms and beats 65.56% of users
Memory: 19.20 MB and beats 88.89% of users

### Description
Reversing the linked list makes it easier to manage because we approach the problem similar to basic multiplication, starting from the smallest digit and progressing to the largest digit. Each digit is multiplied by two, with the carry from the previous digit added to it. This process is efficiently handled within a single while loop outlined in the algorithm. Following the loop, we incorporate a check to determine if there are more digits than the original number had; if there are, we add another node. Finally, to obtain the correct value, we reverse the linked list once more.

### LeetCode Description
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

## Topics
- Linked List
- Math
- Stack
