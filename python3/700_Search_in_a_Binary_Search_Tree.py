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

class Solution:
    # divide conquer
    def searchBST(self, root, val):
        if root is None:
            return None
        
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        
        # BST 的順序是左根右
        # 但是左子樹和右子樹有可能是 None 所以要先判斷
        if left and left.val == val:
            return left
        elif root.val == val:
            return root
        elif right and right.val == val:
            return right
