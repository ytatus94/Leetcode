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
        self.traversal(root, 1) # 當前深度是 1
        return self.max_depth

    # 定義: 把以 root 為根的最大深度記錄下來
    def traversal(self, root, depth):
        # 出口: 處理空節點
        if root is None:
            return
        if self.max_depth < depth:
            self.max_depth = depth
        # 拆解:
        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        self.max_depth = 0
        self.helper(root, 0)
        return self.max_depth

    def helper(self, root, depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.max_depth = max(self.max_depth, depth + 1)
            return
        depth += 1
        self.helper(root.left, depth)
        self.helper(root.right, depth)


# 用 divide conquer 的方法
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # 定義: 傳回以 root 為根的子樹的最大深度
    def max_depth(self, root: TreeNode) -> int:
        depth = 0
        # 出口: 處理空節點
        if root is None:
            return depth
        # 拆解:
        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)
        # 合併:
        depth = max(left_max_depth, right_max_depth) + 1
        return depth

