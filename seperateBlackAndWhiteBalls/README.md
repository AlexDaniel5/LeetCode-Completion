## General Information
Name: Alex Daniel
Date: October 14, 2024

### To Run
- python minimumSteps.py

### Results
Speed: 104 ms and beats 65.12% of users
Memory: 16.48 MB and beats 39.53% of users

### Description
Use two pointers: the first iterates through the string, checking for white balls. If a white ball is found, increment the left pointer, which acts as a counter for zeros. When a black ball is encountered after a white ball, add the count of black balls that need to be swapped with the white ball to ensure the correct order.

## Notes
- I initially planned to count the black balls, but counting the white balls works better, as it allows us to subtract their index from the total number of white balls

### LeetCode Description
There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

# Topics
- Two Pointers
- String
- Greedy