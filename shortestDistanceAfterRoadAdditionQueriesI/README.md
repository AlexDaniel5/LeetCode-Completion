## General Information
Name: Alex Daniel
Date: November 27, 2024

### To Run
- python shortestDistanceAfterQueries.py

### Results
Speed: 728 ms and beats 63.16% of users
Memory: 12.55 MB and beats 23.81% of users

### Description
First, add all the default edges from 0 to n - 1 to initialize the graph. Then, for each query, run a loop to find the fastest path to the destination node after adding the query. In each iteration, we use a deque to track the current node and the number of steps taken to reach it. We also maintain a visited set to avoid revisiting nodes and improve efficiency. The loop continues until the BFS search completes or the destination node is reached.

### LeetCode Description
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

# Topics
- Array
- Breadth-First Search
- Graph