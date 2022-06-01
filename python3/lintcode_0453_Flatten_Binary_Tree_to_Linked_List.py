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

# 用 Traverse
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        self.last_node = None # 要用來記錄左子樹最後一個節點
        self.helper(root)
        return
    
    def helper(self, root):
        if root is None:
            return

        if self.last_node is not None:
            self.last_node.left = None
            # 當 last_node = 1 的時候，這邊把右子樹改成 2 了
            self.last_node.right = root # 這時候 root = 2 是 1 的左子樹

        self.last_node = root
        # 當 last_node = 1 時這裡要記下右子樹是 5
        right_subtree = root.right
        self.helper(root.left) # 這裡會在下個循環中把 1 的右子樹改成 2
        self.helper(right_subtree)

# 用 Divid conquer
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
