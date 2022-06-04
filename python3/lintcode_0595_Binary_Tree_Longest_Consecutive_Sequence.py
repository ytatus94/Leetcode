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
    
    # 定義: 傳回以 root 為根的子樹中，最長的連續路徑長度
    def longest_consecutive(self, root: TreeNode) -> int:
        self.longest_length = 0
        self.helper(root)
        return self.longest_length

    def helper(self, root):
        # write your code here
        # 出口:
        if root is None:
            return 0

        # 拆解:
        left_length = self.helper(root.left)
        right_length = self.helper(root.right)

        current_length = 1 # 現在的長度

        # 下一層節點要比 root 大 1 的時候，長度才會加 1，不然就維持目前最長的長度
        # 有可能左子樹的長度比右子樹的長度還長，所以用 current_length 保留當前最長的長度
        if root.left is not None and root.val + 1 == root.left.val:
            current_length = max(current_length, left_length + 1)
        if root.right is not None and root.val + 1 == root.right.val:
            current_length = max(current_length, right_length + 1)

        # 打擂台
        if self.longest_length < current_length:
            self.longest_length = current_length
        
        return current_length
