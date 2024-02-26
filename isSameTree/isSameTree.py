# Definition for binary tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        # Leaf nodes end at the same time
        if p is None and q is None:
            return True
        # Check if both nodes are equal and return
        # the children nodes recursively to check if they're equal
        if p is not None and q is not None:
            return ((p.val == q.val) and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        # If the leaf nodes end at different times
        return False

solution = Solution()

pTree = TreeNode(1)
pTree.left = TreeNode(2)
pTree.right = TreeNode(3)

qTree = TreeNode(1)
qTree.left = TreeNode(2)
qTree.right = TreeNode(3)

print(solution.isSameTree(pTree, qTree))  # True