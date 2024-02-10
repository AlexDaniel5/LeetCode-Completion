## General Information
Name: Alex Daniel
Date: February 9, 2024

### To Run
- python perfectSquares.py

### Results
Failed Test case 571/588 due to time limit

### Description of Failed Attempt #2
Uses the idea of a tree in which we solve for every value up to n beforehand. However, fails due to time limit.

## Description of Failed Attempt
Calculate all the perfect squares below n. Sum the largest perfect square under n repeatedly while keeping a count until the sum reaches or exceeds n.

### Notes
Range goes up to the second arguement but not including it; we can do + 1 to include it.

### LeetCode Description
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.