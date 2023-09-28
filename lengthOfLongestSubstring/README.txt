Name: Alex Daniel
Date: September 27, 2023
To Run: 
- make
- ./lengthOfLongestSubstring
Speed: O(n)

Description:
Each character has in the input string has its own index within the array 'seen[128]', determined by its ASCII value. This array serves as a record of
when each character was last encountered, and it is updated at the end of each iteration. The algorithm maintains two bounds: a right bound and a left bound.
The right bound is represented by the variable 'i' in the for loop, which consistently increments by one. The left bound is determined on whether the current 
character has been previously encountered. If the character has been seen before, the left bound is shifted to the position immediately after the last occurrence
of that character. However, if the left bound has already surpassed the last occurrence index, it remains unchanged. Throughout each iteration, the algorithm
checks whether the length between the left bound and the right bound is greater than any previous lengths encountered.

LeetCode Description:
Given a string s, find the length of the longest substring without repeating characters.