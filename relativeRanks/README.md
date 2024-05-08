## General Information
Name: Alex Daniel
Date: May 8, 2024

### To Run
- python findRelativeRanks.py

### Results
Speed: 38 ms and beats 94.10% of users
Memory: 12.36 MB and beats 93.06% of users

### Description
First, we maintain an index for each integer, allowing us to subsequently sort this index array according to rank positions. For instance, sorting an index array based on a rank array such as [10, 3, 8, 9, 4] would assign the second index value as 3 because the second rank corresponds to that index. Consequently, as we iterate through the array, we utilize a nested index to allocate the corresponding ranking to that index (e.g., placements[index[1]] = placements[3], resulting in the fourth value being 'Silver Medal'). This process is repeated within a loop to generate the complete result array.

### LeetCode Description
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

### Topics
- Array
- Sorting
- Heap (Priority Queue)