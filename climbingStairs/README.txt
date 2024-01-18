Name: Alex Daniel
Date: January 17, 2024

To Run:
- python climbingStairs.py

Description:
This solution employs a bottom-up dynamic programming approach by starting from the base case (n) and
iteratively determining the number of ways to reach each step by considering the ways to reach the previous
steps. By manually inspecting the initial values (1, 1, 2, 3, 5, 8, 13), a recognizable pattern emerges,
revealing a Fibonacci sequence. Recognizing this pattern, the solution utilizes a simplified Fibonacci
sequence calculation to efficiently compute and return the answer.

LeetCode Description:
ou are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
