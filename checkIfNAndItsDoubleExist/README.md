## General Information
Name: Alex Daniel

Date: Decemeber 1, 2024

### To Run
- python checkIfExist.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 12.15 MB and beats 5.98% of users

### Description
Iterate through each number in the array. First, check if the number already exists in the hashtable; if it does, return True. This initial check is crucial to handle cases where the array contains zero, as zero multiplied or divided by any number equals itself, which could incorrectly appear as a double. Next, add the number divided by two to the hashtable (to account for potential doubles seen earlier) and the number multiplied by two (to account for potential doubles that may appear later). Repeat this process for all numbers in the array. If no match is found, return False, as it indicates no doubles exist.

### LeetCode Description
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

### Topics
- Array
- Hash Table
- Two Pointers
- Binary Search
- Sorting