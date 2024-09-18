## General Information
Name: Alex Daniel
Date: September 17, 2024

### To Run
- python largestNumber.py

### Results
Speed: 17 ms and beats 87.74% of users
Memory: 11.73 MB and beats 40.70% of users
Complexity: O(Nlog(N))

### Description
Convert integers to strings for easier comparison. Use Python's cmp_to_key function with a custom comparison function to sort the array. This function compares concatenated string pairs to determine the optimal order. Join the sorted array into a single string, converting to an integer and back to a string to handle cases with multiple leading zeros.

### Notes
- cmp_to_key: a sorting algorithm that compares each element with every other element using the mycmp() function, which returns a key based on the comparison. This key is then used by sorted() to arrange the elements in ascending order.
- sorted(): Uses Timsort, a hybrid sorting algorithm combining merge sort and insertion sort. It has a time complexity of O(nlog(n))

### LeetCode Description
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

### Topics
- Array
- String
- Greedy
- Sorting