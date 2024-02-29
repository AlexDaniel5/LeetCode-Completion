from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        frontier = deque([root])
        level = 0
        # While there exists a level
        while frontier:
            levelSize = len(frontier)
            prevNode = 1000001 # Maximum node.val + 1
            if level % 2 == 0:
                prevNode = 0 # Minimum node.val - 1
            # For every node on the level
            for i in range(levelSize):
                node = frontier.popleft()
                # If the node doesn't satisfy level conditions return false
                if level % 2 == 0 and (node.val <= prevNode or node.val % 2 == 0) or \
                level % 2 == 1 and (node.val >= prevNode or node.val % 2 == 1):
                    return False
                prevNode = node.val
                # Get the nodes for the next level
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
            level += 1
        return True # All conditions were met