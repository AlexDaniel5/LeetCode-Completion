## General Information
Name: Alex Daniel
Date: February 17, 2024

### To Run
- python furthestBuilding.py

### Results
Speed: 581ms and beats 73.81% of users
Memory: 22.84 MB and beats 52.38% of users

### Description
Initialize a heap to store all the climbs. A heap is suitable for sorting a list of integers from smallest to largest. As climbs
are added to the heap, perform climbs using bricks; if bricks are exhausted, use ladders and add the corresponding brick amount
for using a ladder on the tallest climb. Repeat this process until running out of both bricks and ladders, then return the total
number of iterations.

## Notes
- Heaps offer significantly greater efficiency for maintaining a dynamically sorted collection compared to using a regular list.

### LeetCode Description
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.