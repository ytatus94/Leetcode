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
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def remove_node(self, root: TreeNode, value: int) -> TreeNode:
        # write your code here
        if root is None:
            return None

        if root.val == value:
            # 當左右子樹都是空，那就把 root 刪除
            # 當左子樹是空，就去右子樹中找最小值，搬到 root 的位置，再用遞迴的方式把右子樹中的最小值刪除
            # 當右子樹是空，就去左子樹中找最大值，搬到 root 的位置，再用遞迴的方式把左子樹中的最大值刪除
            if root.left is None and root.right is None:
                root = None
            elif root.right is None:
                max_node = self.find_bst_max(root.left)
                root.val = max_node.val
                root.left = self.remove_node(root.left, max_node.val) # 左子樹的結構改變了
            else:
                min_node = self.find_bst_min(root.right)
                root.val = min_node.val
                root.right = self.remove_node(root.right, min_node.val) # 右子樹的結構改變了

            return root

        # value 比 root 小，就去左子樹中尋找
        # value 比 root 大，就去右子樹中尋找
        if value < root.val:
            root.left = self.remove_node(root.left, value)
        elif value > root.val:
            root.right = self.remove_node(root.right, value)

        return root

    def find_bst_min(self, root):
        if root is None:
            return None
        # bst 的最小值一定是在左子樹，所以要一直往左找
        if root.left is None:
            return root
        else:
            return self.find_bst_min(root.left)

    def find_bst_max(self, root):
        if root is None:
            return None
        # bst 的最大值一定是在右子樹，所以要一直往右找
        if root.right is None:
            return root
        else:
            return self.find_bst_max(root.right)
