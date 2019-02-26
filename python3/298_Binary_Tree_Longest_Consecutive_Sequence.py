# lintcode 595
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
    def longestConsecutive(self, root):
        # write your code here
        self.longest = 0
        self.helper(root)
        return self.longest
        
    # 傳回以 root 為根的子樹的最長序列的長度
    def helper(self, root):
        if root is None:
            return 0
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        subtree_longest = 1 # 自己的長度
        
        # 判斷左右子樹是否是空
        # 如果不是空，要看左右子樹和 root 的值是否差 1 (子樹的數值要比 root 大才行)
        if root.left is not None and root.val + 1 == root.left.val:
            subtree_longest = max(subtree_longest, left + 1)
        if root.right is not None and root.val + 1 == root.right.val:
            subtree_longest = max(subtree_longest, right + 1)
            
        if subtree_longest > self.longest:
            self.longest = subtree_longest
            
        return subtree_longest
