## General Information
Name: Alex Daniel
Date: February 27, 2024

### To Run
- python diameterOfBinaryTree.py

### Results
Speed: 23ms and beats 75.40% of users
Memory: 14.54 MB and beats 55.42% of users

### Description
The program  employs a recursive depth-first traversal to find the depth of each subtree while updating the longest path encountered so far. The depth of each subtree is determined by adding 1 to the maximum depth between its left and right subtrees. The final result, representing the diameter, is stored in the self.diameter attribute and returned after the traversal.

## Notes
- I cannot recursively call the original function directly because the method should invoke the current instance using self. Consequently, self.longestLength is shared among all methods within the class, ensuring accessibility throughout the object's lifecycle.

### LeetCode Description
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
