# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, result):
            # Base case
            if not node:
                return 0
            # Shift current value left one
            result = result * 10 + node.val
            # Found leaf node return
            if not node.left and not node.right:
                return result
            # Continue recursion with children
            return dfs(node.left, result) + dfs(node.right, result)
        return dfs(root, 0)
    
tree = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))

print(Solution().sumNumbers(tree)) # 1026