"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        if root is None:
            return
        
        for node in root.children:
            self.helper(node, result)
            
        result.append(root.val)
        
    # divide conquer
    def postorder(self, root):
        if root is None:
            return []
        res = []
        for node in root.children:
            res += self.postorder(node)
        res.append(root.val)
        return res
