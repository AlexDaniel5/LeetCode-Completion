## General Information
Name: Alex Daniel
Date: February 14, 2024

### To Run
- python largestPerimeter.py

### Results
Speed: 493ms and beats 98.21% of users
Memory: 26.62 MB and beats 94.62% of users

### Description
Start by sorting the list and obtaining the sum of its elements; these are fundamental steps for solving the problem. Then, iterate through
the sorted list from the largest to the smallest number. During the iteration, compare the largest number (representing the longest side) to
the sum of the remaining elements in the list (forming a potential polygon). If the largest number is greater, it indicates that a valid
polygon cannot exist, so remove it and continue iterating through the updated list. Otherwise, consider the polygon as completed. To conclude,
verify if the resulting polygon has three sides to ensure it forms a proper shape.

## Notes
- I spent a considerable amount of time attempting to iterate from the smallest to the largest item in the list. However, I abandoned this
approach due to the complexity it introduced. Here's a way to picture the issue, say we're adding the 12th element to the sum which is equal
to the first 11 elements, this is valid if the shape has 13 sides as it can have small sides with equal length. On the contrary, if the 12th
element is the last side added, it must be removed as it equals the rest of the sides, forming an invalid polygon. This process of potentially
removing elements could repeat all the way to the beginning of the list, meaning the creation of an additional for loop for continuous removal.
Recognizing this issue I realized I can iterate through the list backwards and not have this problem since we know what the potentially largest
side from the start.

### LeetCode Description
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
