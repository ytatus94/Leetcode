"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    # Traverse + divide conquer
    def longestConsecutive2(self, root):
        # write your code here
        self.longest = 0
        self.helper(root)
        return self.longest
        
    # 傳回以 root 為根的子樹中連續遞增和遞減的最大值
    def helper(self, root):
        if root is None:
            return 0, 0
            
        left_inc_max, left_dec_max = self.helper(root.left)
        right_inc_max, right_dec_max = self.helper(root.right)
        
        # 當前節點長度
        max_increase, max_decrease = 1, 1
        
        # 由 root 來看
        # 1. 可能左子樹遞增，右子樹遞減
        if root.left is not None and root.val + 1 == root.left.val:
            max_increase = max(max_increase, left_inc_max + 1)
        if root.right is not None and root.val - 1 == root.right.val:
            max_decrease = max(max_decrease, right_dec_max + 1)
            
        # 2. 可能左子樹遞減，右子樹遞增
        if root.left is not None and root.val - 1 == root.left.val:
            max_decrease = max(max_decrease, left_dec_max + 1)
        if root.right is not None and root.val + 1 == root.right.val:
            max_increase = max(max_increase, right_inc_max + 1)
            
        self.longest = max(self.longest, max_increase + max_decrease - 1)
        
        return max_increase, max_decrease
