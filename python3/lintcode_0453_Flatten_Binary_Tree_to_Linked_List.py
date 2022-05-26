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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        # 注意這個方程式不回傳任何東西
        # 所以要對 root 的子樹直接做 inplace 的修改
        self.helper(root)

    # 定義: 傳回以 root 為根的 linked list 的最後一個點
    # 因為需要最後一個點去接上另一個子樹的第一個點
    def helper(self, root):
        # 出口:
        if root is None:
            return None

        # 拆解:
        left_last_node = self.helper(root.left)
        right_last_node = self.helper(root.right)

        if left_last_node is not None:
            left_last_node.right = root.right
            root.right = root.left
            root.left = None

        if right_last_node is not None:
            return right_last_node
        elif left_last_node is not None:
            return left_last_node

        return root
