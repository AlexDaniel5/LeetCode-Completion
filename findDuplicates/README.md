## General Information
Name: Alex Daniel
Date: March 25, 2024

### To Run
- python findDuplicates.py 

### Results
Speed: 244 ms and beats 95.42% of users
Memory: 20.35 MB and beats 50.80% of users

### Description
Iterate through the array, adding each number to a set for faster search times compared to an array. As we traverse the array, check if each number already exists in the set; if it does, add it to a separate array. This method is effective because numbers in the array cannot appear more than twice; otherwise, a hash map would be necessary for counting occurrences accurately.

### LeetCode Description
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

## Topics
- Array
- Hash Table
