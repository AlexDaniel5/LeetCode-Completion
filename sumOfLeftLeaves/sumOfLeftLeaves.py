from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        result = 0
        frontier = deque([root])
        # While the queue isn't empty continue BFS search
        while frontier:
            node = frontier.popleft()
            if node.right:
                frontier.append(node.right)
            if node.left:
                # If this is a left leaf add it to the result
                if not node.left.right and not node.left.left:
                    result += node.left.val
                else:
                    frontier.append(node.left)
        return result

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))) # 24
print(Solution().sumOfLeftLeaves(tree))