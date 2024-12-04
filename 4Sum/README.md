## General Information
Name: Alex Daniel

Date: Decemeber 4, 2024

### To Run
- python fourSum.py 

### Results
Speed: 432 ms and beats 90.27% of users
Memory: 12.52 MB and beats 5.85% of users
Time Complexity: O(N³): Iterate through the list for the first number in the four-sum (excluding the last three values), then for the second number (excluding the last two values), and finally use a two-pointer approach to find the last two numbers.

### Description
First, we sort the array. Then, we select the first two numbers using a loop, starting with the leftmost values, and subtract their sum from the target value. These two numbers are added to a temporary list. Next, we use a two-pointer approach to find all possible combinations of the remaining numbers that add up to the adjusted target, similar to the two-sum problem. Once all combinations for the current pair are found, we remove the second number from the list quad and try the next value as the second number in the list quad. We repeat this process until all combinations using the first number are explored. After completing this iteration for the first number, we repeat the process starting with the next number as the first value.

### LeetCode Description
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

## Topics
- Array
- Two Pointers
- Sorting