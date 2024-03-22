## General Information
Name: Alex Daniel
Date: March 22, 2024

### To Run
- python isPalindrome.py

### Results
Speed: 621 ms and beats 93.73% of users
Memory: 64.93 MB and beats 91.14% of users

### Description
Converting a linked list into an array list can be less efficient than employing a more streamlined approach. One such approach involves finding the middle point of the linked list using a technique where one pointer moves at twice the speed of another (a strategy inspired by Floyd's algorithm). Next, reverse the linked list, a process similar to what was tackled in yesterday's LeetCode challenge. Subsequently, compare the two resulting linked lists to determine if they are identical. We assess the equality when the right linked list pointer reaches null, recognizing that the left linked list retains the data from both halves and remains intact.

### LeetCode Description
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.