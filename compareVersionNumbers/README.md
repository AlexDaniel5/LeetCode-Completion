## General Information
Name: Alex Daniel
Date: May 3, 2024

### To Run
- python compareVersion.py

### Results
Speed: 8ms and beats 59.26% of users
Memory: 11.59 MB and beats 93.66% of users

### Description
Convert the given versions into lists using the split() function, breaking them down into segments. Initiate a loop based on the longer length between the two lists to ensure all segments are compared. During each iteration, convert the respective segment to an integer. If a segment doesn't exist in one list, assign a value of 0 to it, reflecting the flexibility in extending any version with an infinite sequence of zeros; for instance, 1.00.000.000. Compare the segments, recognizing that a higher segment in value translates to a higher version number. If any segment comparison yields a definitive result, return that result. This method conveniently mirrors how numeric values operate, with the leftmost digits carrying more significance. If the loop completes without returning a result, it indicates that all corresponding segments are equal, leading to a return value of 0.

## Notes
- Don't forget the beloved split() function

### LeetCode Description
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

### Topics
- String
- Two Pointers