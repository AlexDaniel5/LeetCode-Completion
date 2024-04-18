# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        # Special case, add row immediately 
        if depth == 1:
            updatedRoot = TreeNode(val)
            updatedRoot.left = root
            return updatedRoot
        
        def dfs(node, cur):
            if not node:
                return
            # If we're before the depth where a row is added add the row
            elif cur == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return
            # Continue searching through the tree until we reach the correct depth
            else:
                dfs(node.left, cur+1)
                dfs(node.right, cur+1)

        dfs(root, 1)
        return root

tree1 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
tree2 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
tree1 = Solution().addOneRow(tree1, 1, 3)
tree2 = Solution().addOneRow(tree1, 1, 1)

# Helper function to print trees
def printTree(root, level=0, prefix="Root:"):
    if root is None:
        return
    print(" " * level + prefix, root.val)
    printTree(root.left, level+1, "L:")
    printTree(root.right, level+1, "R:")

print("Tree 1:")
printTree(tree1)
print("Tree 2:")
printTree(tree2)