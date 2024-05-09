## General Information
Name: Alex Daniel
Date: May 9, 2024

### To Run
- python maximumHappinessSum.py

### Results
Speed: 815 ms and beats 90.33% of users
Memory: 33.11 MB and beats 88.66% of users

### Description
First, sort the array. Then, iterate through the array, decrementing k each iteration and stopping once k is zero. In each iteration, subtract the iteration count from the child and check if the child is a non-positive integer; if so, return the total. Then, in the iteration, add the child's happiness to the total.

### LeetCode Description
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

### Topics
- Array
- Greedy
- Sorting