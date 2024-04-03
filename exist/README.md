## General Information
Name: Alex Daniel
Date: April 3, 2024

### To Run
- python exist.py 

### Results
Speed: 6011 ms and beats 61.55% of users
Memory: 11.70 MB and beats 54.52% of users

### Description
Utilize a set to maintain a record of visited nodes. Next, iterate through each index within the matrix to verify if it matches the initial character of the target word. If a match is found, employ depth-first search along with recursion to ascertain the feasibility of forming a valid path to spell out the entire word from that point onwards.

## Notes
- When adding or removing from path use double brackets to infer a tuple.

### LeetCode Description
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Topics
- Array
- String
- Backtracking
- Matrix
