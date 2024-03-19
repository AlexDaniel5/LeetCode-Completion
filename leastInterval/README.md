## General Information
Name: Alex Daniel
Date: March 19, 2024

### To Run
- python getCommon.py

### Results
Speed: 296 ms and beats 85.20% of users
Memory: 13.80 MB and beats 71.84% of users

### Description
Determine the occurence of each task, and the number of tasks with the same maximum count. Then using this information we use a formula which considers the critical task's maximum frequency (maxCount) to determine idle slots between executions and accounts for additional tasks (maxOccurrences) that can be scheduled without idle time, optimizing task scheduling and minimizing overall execution time.

### LeetCode Description
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

## Topics
- Heap (Priority Queue)
- Sorting
- Counting
- Array
- Greedy