from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        allSums = []
        q = deque([root])
        
        # BFS search of the binary tree
        while q:
            levelSum = 0
            # Go through all the nodes in the current level
            for i in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                # Add nodes for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add the total value of the level to a list
            allSums.append(levelSum)
        # If there are less levels than k, return -1
        if len(allSums) < k:
            return -1
        allSums.sort()
        return allSums[-k]
    
print(Solution().kthLargestLevelSum([5,8,9,2,1,3,7], 4)) # -1
print(Solution().kthLargestLevelSum([[1,2,None,3], 1])) # 3