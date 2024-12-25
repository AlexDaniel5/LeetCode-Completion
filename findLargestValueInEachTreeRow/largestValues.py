from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def largestValues(self, root):
        # Edge case
        if root is None:
            return []
        largNums = []
        q = deque([root])
        while q:
            largestNum = float('-inf')
            # Go through all the nodes in the current level
            for i in range(len(q)):
                node = q.popleft()
                # Check if the current node is the largest node in the level
                if largestNum < node.val:
                    largestNum = node.val
                # Add nodes for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            largNums.append(largestNum)
        return largNums
    
tree = TreeNode(0)
tree.left = TreeNode(-1)
print(Solution().largestValues(tree)) # [0, -1]