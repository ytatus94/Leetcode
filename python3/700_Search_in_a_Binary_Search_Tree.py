# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.subtree = None
        self.helper(root, val)
        return self.subtree
    
    def helper(self, root, val):
        if root is None:
            return
        
        self.helper(root.left, val)
        if root.val == val:
            self.subtree = root
        self.helper(root.right, val)
