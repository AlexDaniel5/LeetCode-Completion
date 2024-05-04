## General Information
Name: Alex Daniel
Date: May 4, 2024

### To Run
- python numRescueBoats.py

### Results
Speed: 349 ms and beats 62.16% of users
Memory: 16.91 MB and beats 71.04% of users

### Description
Sort the list of people in ascending order based on their weight. Iterate through the sorted list, removing the heaviest person and decrementing the right pointer. After each removal, check if the boat can fit the lightest person as a pair, and if so, increment the left pointer. Continue this process until the right pointer is less than the left pointer, indicating that the entire list has been iterated through and all possible pairings based on weight constraints have been evaluated.

### LeetCode Description
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

### Topics
- Array
- Sorting
- Greedy
- Two Pointers