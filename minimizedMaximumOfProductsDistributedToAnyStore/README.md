## General Information
Name: Alex Daniel
Date: November 14, 2024

### To Run
- python minimizedMaximum.py

### Results
Speed: 575 ms and beats 100.00% of users
Memory: 19.38 MB and beats 100.00% of users

### Description
The solution uses binary search to efficiently find the target number. The possible range for the maximum number of products per store is between 1 and the largest quantity. For each candidate number within this range, we check if it's possible to distribute products such that no store exceeds this number. This process continues until we find the minimized maximum number of products per store.

### LeetCode Description
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

    A store can only be given at most one product type but can be given any amount of it.
    After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

Return the minimum possible x.

### Topics
- Array
- Binary Search