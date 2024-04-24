## General Information
Name: Alex Daniel
Date: April 23, 2024

### To Run
- python tribonacci.py

### Results
Speed: 7 ms and beats 94.93% of users
Memory: 11.86 MB and beats 12.75% of users

### Description
First, we handle the base case to check if the input is 0, 1, or 2, as these are the starting values in the Tribonacci sequence. If the input is not a base case, we iterate a loop n-3 times; three fewer occurrences because we've already looped for the base case. Within this loop, we set each element to the next element in the array, and the final element of the array to the total of the current array.  Overall, this problem is akin to the Fibonacci sequence but with a different recurrence relation.

### LeetCode Description
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

### Topics
- Math
- Dynamic Programming
- Memoization