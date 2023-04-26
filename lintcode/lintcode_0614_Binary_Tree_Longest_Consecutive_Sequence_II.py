from lintcode import (
    TreeNode,
)

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
    def longest_consecutive2(self, root: TreeNode) -> int:
        # write your code here
        self.longest_length = 0
        self.helper(root)
        return self.longest_length

    def helper(self, root):
        if root is None:
            return 0, 0

        left_inc, left_dec = self.helper(root.left)
        right_inc, right_dec = self.helper(root.right)

        curr_inc, curr_dec = 1, 1

        if root.left is not None and root.val + 1 == root.left.val:
            curr_inc = max(curr_inc, left_inc + 1)
        if root.right is not None and root.val - 1 == root.right.val:
            curr_dec = max(curr_dec, right_dec + 1)

        if root.left is not None and root.val - 1 == root.left.val:
            curr_dec = max(curr_dec, left_dec + 1)
        if root.right is not None and root.val + 1 == root.right.val:
            curr_inc = max(curr_inc, right_inc + 1)

        self.longest_length = max(self.longest_length, curr_inc + curr_dec - 1)

        return curr_inc, curr_dec
