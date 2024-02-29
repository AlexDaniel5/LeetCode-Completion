from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        frontier = deque([root])
        # While the queue isn't empty continue BFS search
        while frontier:
            node = frontier.popleft()
            if node.right:
                frontier.append(node.right)
            if node.left:
                frontier.append(node.left)
        return node.val
    
solution = Solution()
tree = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution.findBottomLeftValue(tree))
