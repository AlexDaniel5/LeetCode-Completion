# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
        def diameterOfBinaryTree(self, root):
            self.longestLength = 0
            def depth(node):
                # Base case: if the node is None
                if not node:
                    return 0
                # Recursively calculate the depth of the left and right subtrees
                leftDepth = depth(node.left)
                rightDepth = depth(node.right)
                # Update longestLength with the sum of left and right depths if it's greater
                if leftDepth + rightDepth > self.longestLength:
                    self.longestLength = leftDepth + rightDepth
                # As the recursion unwinds, the depth of the current subtree is determined
                # Adding 1 represents the depth of the current node.
                return 1 + max(leftDepth, rightDepth)
            # Start the recursive depth calculation from the root of the tree
            depth(root)
            return self.longestLength

solution = Solution()
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(solution.diameterOfBinaryTree(tree1))  # 3

