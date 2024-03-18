## General Information
Name: Alex Daniel
Date: March 18, 2024

### To Run
- python findMinArrowShots.py 

### Results
Speed: 1082 ms and beats 33.57% of users
Memory: 61.08 MB and beats 60.52% of users

### Description
First, sort the lists. Then, set the answer to the number of intervals. Iterate through each array and check if two intervals overlap. If they do, remember the end of the minimum interval for comparison in the next iteration. Subtract one from our answer in this case, as it means an arrow can hit two balloons. Otherwise, remember the beginning of the interval for the next iteration.

### LeetCode Description
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

## Topics
- 2D arrays
- Intervals
- Sorting
