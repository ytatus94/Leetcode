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
# 用 traversal 的方法
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        self.max_depth = 0
        self.traversal(root, 1)
        return self.max_depth

    def traversal(self, root, depth):
        if root is None:
            return
        if self.max_depth < depth:
            self.max_depth = depth

        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)

# 用 divide conquer 的方法
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # 定義: 傳回以 root 為根的子樹的最大深度
    def max_depth(self, root: TreeNode) -> int:
        depth = 0
        # 出口:
        if root is None:
            return depth
        # 拆解:
        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)
        depth = max(left_max_depth, right_max_depth) + 1
        return depth

