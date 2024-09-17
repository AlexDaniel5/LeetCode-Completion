## General Information
Name: Alex Daniel
Date: September 6, 2024

### To Run
- python uncommonFromSentences.py

### Results
Speed: 8 ms and beats 96.74% of users
Memory: 11.69 MB and beats 73.00% of users

### Description
Combine the two sentences into one large string, ensuring that a space is added between them to avoid merging adjacent words. Use the split() function to break this string into an array of words. Count the occurrences of each word using a dictionary. Finally, return an array containing only the words that appear exactly once in the hash table.

### LeetCode Description
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Topics
- Hash table
- String
- Counter