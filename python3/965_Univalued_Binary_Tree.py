# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isUnival = True        
        self.helper(root, root.val)
        return self.isUnival

    def helper(self, root, val):
        if root is None:
            return
        
        if root.val != val:
            self.isUnival = False
            
        self.helper(root.left, val)
        self.helper(root.right, val)
