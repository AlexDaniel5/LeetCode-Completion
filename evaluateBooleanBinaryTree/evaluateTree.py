# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def evaluateTree(self, root):
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        # Or operator
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # And operator
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
# Helper function to visualize trees
def printTree(root, level=0, prefix="Root:"):
    if root is None:
        return
    print(" " * level + prefix, root.val)
    printTree(root.left, level+1, "L:")
    printTree(root.right, level+1, "R:")

tree = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
print("Tree:")
printTree(tree)
print(Solution().evaluateTree(tree)) # True