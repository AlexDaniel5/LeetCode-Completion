## General Information
Name: Alex Daniel
Date: April 30, 2024

### To Run
- python threeSum.py

### Results
Speed: 726 ms and beats 88.43% of users
Memory: 15.46 MB and beats 26.16% of users
Time: O(nlog(n)) + (n²) Sorting (nlog(n)) plus one loop to determine the first value and a nested loop for the two sum (n²)

### Description
First, start by sorting the array. Then, utilize a nested loop structure. The outer loop handles the first value of the triple sum, tracking its index to facilitate determining the left interval's value for the second element. Within the nested loop, explore all possible number combinations with the first value and sum them. When the sum exceeds 0, decrement the right pointer to shrink the sum; if the sum is less than zero, increment the left pointer to expand it. If the sum equals zero, add it to the result array and increment the left pointer for further evaluation. 


### Notes
- When incrementing a pointer, check if it equals the previous value. If so, increment it again. This precaution ensures that if consecutive equal numbers occur, the resulting arrays won't treat them as separate values, preventing duplication of results

### LeetCode Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Topics
- Array
- Two Pointers
- Sorting