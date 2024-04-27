## General Information
Name: Alex Daniel
Date: April 27, 2024

### To Run
- python maxArea.py 

### Results
Speed: 505 ms and beats 88.28% of users
Memory: 21.97 MB and beats 97.34% of users
Time: O(n)

### Description
Start by setting a left and right window at both ends of the container. Calculate the initial maximum area by multiplying the minimum height of the two windows by the width of the container. Then, use a while loop to determine all maximum areas efficiently. Ensure the loop ends when the right and left windows equal each other to avoid redundant calculations and negative areas (without using abs()). Crucially, always move the window with the lower height during each iteration. This prioritizes moving the lower height as it determines the overall height. Finally, return the highest area obtained from this process.

### LeetCode Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Topics
- Array
- Two Pointers
- Greedy
