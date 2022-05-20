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

# 用 Traversal 的寫法
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        result = []
        self.traversal(root, result) # traversal 是把結果當參數傳遞
        return result
        
    # 把以 root 為根的 preorder 放到 result 裡面去
    def traversal(self, root, result):
        # 遞歸的出口: 處理空節點
        # 空節點時 ==> 什麼都不做
        if root is None:
            return
        result.append(root.val)
        self.traversal(root.left, result)
        self.traversal(root.right, result)

# 用 Divider conquer
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    # 定義: 傳回以 root 為根的 preorder
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        # 出口: 處理空節點
        if root is None: 
            return result

        # 拆解:
        left = self.preorder_traversal(root.left)
        right = self.preorder_traversal(root.right)

        result.append(root.val)
        result += left
        result += right
        return result
