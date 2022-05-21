from typing import (
    List,
)
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

# 用 Traversal 的方法
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        result = []
        self.traversal(root, result)
        return result
    
    # 定義: 把以 root 爲根的 inorder 放到 result 裡面
    def traversal(self, root, result):
        # 出口: 處理空節點
        if root is None:
            return
        # 拆解:
        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)
        
# 用 Divide conquer 的方法
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        # 出口:
        result = []
        if root is None:
            return result
        # 拆解:
        left = self.inorder_traversal(root.left)
        right = self.inorder_traversal(root.right)
        # 合併:
        result += left
        result.append(root.val)
        result += right

        return result
