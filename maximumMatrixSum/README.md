## General Information
Name: Alex Daniel
Date: Novemeber 28, 2024

### To Run
- python maxMatrixSum.py

### Results
Speed: 55 ms and beats 94.66% of users
Memory: 18.37 MB and beats 5.65% of users

### Description
By rearranging negatives, any matrix can be adjusted to include zero or one negative number. The solution involves counting the negatives and identifying the smallest absolute value. Iterate through the matrix to calculate the sum, the count of negative numbers, and the smallest absolute value. If the count of negatives is odd, one cannot be rearranged into a positive. In this case, subtract the smallest absolute value from the sum twice: once to remove its contribution and again to account for its adjusted value.

### LeetCode Description
You are given an n x n integer matrix. You can do the following operation any number of times:

    Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

### Topics
- Array
- Greedy
- Matrix