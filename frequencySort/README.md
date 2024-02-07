## General Information
Name: Alex Daniel
Date: February 7, 2024

### To Run
- python frequencySort.py

### Results
Speed: 24ms and beats 86.75% of users
Memory: 13.84 MB and beats 98.29% of users

### Description
First, obtain the character count for each character in the given string. Next, arrange the character counts in descending order.
Finally, construct an output string by appending each character multiplied by its corresponding count in the sorted order.

### Notes
The sorted() function in Python is a versatile sorting tool applicable to various objects. It takes three arguments:
- The first argument is the data to be iterated through.
- The second argument is a helper function that guides the sorting process.
- The third argument indicates whether to sort in reverse order.
The second argument is noteworthy. In this context, we employ a special approach by utilizing an anonymous sorting function (lambda).
This function is designed to retrieve the item being sorted (the tuple x) and extract its second element (the value) for the sorting
comparison.

### LeetCode Description
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
