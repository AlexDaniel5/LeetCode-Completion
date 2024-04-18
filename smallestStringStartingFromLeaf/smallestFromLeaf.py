class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, result):
            # Converts an integer into a character and adds it to the string
            result = chr(97 + node.val) + result
            # If both subtrees exist, return the smallest result
            if node.left and node.right:
                return min(dfs(node.left, result), dfs(node.right, result))
            # Continue iterating through the tree
            elif node.right:
                return dfs(node.right, result)
            elif node.left:
                return dfs(node.left, result)
            return result
        return dfs(root, "")
    
tree = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
print(Solution().smallestFromLeaf(tree)) # dba