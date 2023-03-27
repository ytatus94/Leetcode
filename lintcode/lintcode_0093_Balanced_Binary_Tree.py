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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        balanced, depth = self.helper(root)
        return balanced
        

    # 定義: 傳回以 root 為根的子樹是否是平衡樹，還有樹的深度
    # 如果不是平衡樹，那就不用管深度直接回傳 False
    def helper(self, root):
        # 出口:
        if root is None:
            return True, 0
        # 拆解:
        left_balanced, left_depth = self.helper(root.left)
        right_balanced, right_depth = self.helper(root.right)

        if left_balanced and right_balanced: # 左右子樹都必須要是平衡樹
            if abs(left_depth - right_depth) <= 1: # 左右子樹的高度差要 <= 1
                current_depth = max(left_depth, right_depth) + 1
                return True, current_depth
        return False, -1

