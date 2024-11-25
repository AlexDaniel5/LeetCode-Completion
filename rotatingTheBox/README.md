## General Information
Name: Alex Daniel
Date: November 25, 2024

### To Run
- python arotateTheBox.py

### Results
Speed: 1722 ms and beats 83.00% of users
Memory: 71.08 MB and beats 5.34% of users

### Description
In this algorithm, I iterate through each cell of the matrix from top-left to bottom-right. A right pointer is used to track where stones can fall, updating whenever an obstacle is encountered or a stone is moved. When a stone is found, the right pointer shifts one position to the left, and a swap is attempted with the current position. After processing all rows, the matrix is rotated 90 degrees clockwise to achieve the desired final state.

## Notes
- list(map(list, zip(*reversed(box)))): The asterisk unpacks the matrix into a list of lists. zip() re-aggregates the arguements into column-wise tuples. map (list, ...) then converts each tuple into a list. Finally, list(map(...)) converts the object into a list of lists. Overall, this rotates the matrix 90 degress clockwise.
- There is certainly a more memory-efficient approach to this problem: instead of rotating the matrix at the end, we can directly fill a new matrix with pre-rotated dimensions as we process the input. This eliminates the need for an additional rotation step and reduces intermediate memory usage

### LeetCode Description
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

## Topics
- Array
- Two Pointers
- Matrix