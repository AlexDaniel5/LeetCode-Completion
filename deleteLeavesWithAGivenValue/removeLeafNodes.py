# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        stack = [root]
        visit = set()
        parents = {root: None}
        while stack:
            node = stack.pop()
            # Check if the node is a leaf node
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            else:
                if node not in visit:
                    visit.add(node)
                    stack.append(node)  # Re-add the node to handle it after children
                    # Process the children
                    if node.right:
                        stack.append(node.right)
                        parents[node.right] = node
                    if node.left:
                        stack.append(node.left)
                        parents[node.left] = node        
        return root