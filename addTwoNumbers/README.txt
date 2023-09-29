Name: Alex Daniel
Date: September 28, 2023

To Run:
- make
- ./addTwoNumbers

Idea:
Reverse the linked list to make the nodes form the number left to right. Then convert the linked lists into integers
which we can take the sum of. Finally, convert the sum into a list so we can grab each digit as an index and convert them
back into nodes. which would be returned.

Failure Reason:
To convert the linked list into an integer we need the digit (node) by the digit holder it'll place in. However, if the number
is too large signed integer overflow occurs. We can convert this to an unsigned integer but this only brings us so much farther.

Test case 1554 failed:
Input
l1 =
[9]
l2 =
[1,9,9,9,9,9,9,9,9,9]
Use Testcase
Output
[8,0,4,5,6,0,0,1,4,1]
Expected
[0,0,0,0,0,0,0,0,0,0,1]


LeetCode Description:
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.