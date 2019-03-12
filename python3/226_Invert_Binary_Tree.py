# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        left = root.left
        right = root.right
        
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root
