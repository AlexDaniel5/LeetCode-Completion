## General Information
Name: Alex Daniel

Date: December 12, 2024

### To Run
- python pickGifts.py

### Results
Speed: 11 ms and beats 95.45% of users
Memory: 12.40 MB and beats 20.55% of users
Time: KLog(n)

### Description
It's best to use a max-heap structure for this problem. Since Python's heapq module implements a min-heap by default, we convert the list into its negative counterpart. This effectively simulates a max-heap, where the most negative number is at the root (which corresponds to the largest number in the original list).

Next, we iterate through the heap, square-rooting the largest element (the root of the heap) and converting it back to its negative value before pushing it back into the heap. We repeat this process k times. Finally, we return the sum of the positive values from the heap.

### LeetCode Description
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

    Choose the pile with the maximum number of gifts.
    If there is more than one pile with the maximum number of gifts, choose any.
    Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.

Return the number of gifts remaining after k seconds.

# Topics
- Array
- Heap (Priority Queue)
- Simulation