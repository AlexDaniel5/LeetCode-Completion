## General Information
Name: Alex Daniel

Date: December 17, 2024

### To Run
- python repeatLimitedString.py

### Results
Speed: 505 ms and beats 60.00% of users
Memory: 14.14 MB and beats 57.14% of users
Time Complexity: O(N*Log(N))

### Description
Since 'z' has the largest ASCII value in the alphabet, we cannot use a min-heap to sort the letters in reverse order. Instead, we use a max-heap to process the alphabet in descending order.

First, we count the frequency of each character in the string and store each character along with its count as a tuple in the heap. As we process the heap, we remove the top tuple and append the corresponding characters to a result list for efficiency.

If the character count exceeds the repeat limit, we add one of the next character from the heap to break the sequence. Afterward, we push the remaining counts of both characters back into the heap. However, whenever we add one character to break the sequence, we must check if the heap is empty. An empty heap indicates there are no more characters available, and we can safely complete the result string.

### LeetCode Description
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# Topics
- Array
- String
- Greedy
- Heap (Priority Queue)
- Counting