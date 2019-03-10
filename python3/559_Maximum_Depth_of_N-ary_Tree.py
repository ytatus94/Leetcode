"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.depth = 0
        self.helper(root, 1)
        return self.depth
    
    def helper(self, root, curr_depth):
        if root is None:
            return
        
        if self.depth < curr_depth:
            self.depth = curr_depth
        
        for node in root.children:
            self.helper(node, curr_depth + 1)
