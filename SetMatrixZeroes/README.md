## General Information
Name: Alex Daniel

Date: May 20, 2024

### To Run
- python setZeroes.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 13.24 MB and beats 23.45% of users
Time: O(M * N)

### Description
Use the first row and first column as markers to indicate which rows and columns should be set to zero. Traverse the matrix once to record these markers based on the location of any zeroes. Then, make a second pass through the matrix to update the cells to zero according to the markers. Finally, update the first row and first column themselves using separately stored boolean flags to reflect their original state, since they were used to store marker information.

### LeetCode Description
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

# Topics
- Array
- Hash Table
- Matrix