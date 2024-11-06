## General Information
Name: Alex Daniel
Date: Novemeber 6, 2024

### To Run
- python canSortArray.py 

### Results
Speed: 6 ms and beats 100.00% of users
Memory: 11.58 MB and beats 69.23% of users

### Description
To solve this problem, we approach it by dividing the array into sections based on the number of set bits (1s) in each number's binary representation. If several consecutive numbers have the same number of set bits, we can guarantee that this section can be sorted independently. However, if the next number has a different number of set bits, it can’t be sorted along with the previous section. For two sections to be sorted together without issues, the smallest number in the current section must be greater than the largest number in the previous section. We continue this process, checking and comparing sections as we iterate through the array. At the end, we confirm that the last section also follows this rule, ensuring that the smallest number of the current section is greater than the largest number of the previous one.

### Notes
- bin() converts a number into its binary version

### LeetCode Description
You are given a 0-indexed array of positive integers nums.

In one operation, you can swap any two adjacent elements if they have the same number of
set bits
. You are allowed to do this operation any number of times (including zero).

Return true if you can sort the array, else return false.

## Topics
- Array
- Bit Manipulation
- Sorting