## General Information
Name: Alex Daniel
Date: November 22, 2024

### To Run
- python maxEqualRowsAfterFlips.py

### Results
Speed: 51ms and beats 86.67% of users
Memory: 14.00 MB and beats 20.00% of users

### Description
Use a hashmap to count the occurrences of each row. Additionally, flip each row and add the flipped version to the count in the hashmap. Since arrays cannot be used directly as keys in a hashmap, each row is converted into a tuple, which can be used as a key. Finally, return the highest count among all unique keys.

## Notes
- defaultdic(): Allows me to initalize the value of a key to 0, thus faster without the manual checks for initalization

### LeetCode Description
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

## Topics
- Array
- Hash Table
- Matrix