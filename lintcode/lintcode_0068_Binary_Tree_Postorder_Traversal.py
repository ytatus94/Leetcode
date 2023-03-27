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

# 用 traversal 的方法
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        result = []
        self.traversal(root, result)
        return result

    # 定義: 把以 root 為根的 postorder 放到 result 裡面
    def traversal(self, root, result):
        # 出口: 處理空節點
        if root is None:
            return result
        # 拆解:
        self.traversal(root.left, result)
        self.traversal(root.right, result)
        result.append(root.val)
        
# 用 divide conquer 的方法
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        # 出口:
        if root is None:
            return result
        # 拆解:
        left = self.postorder_traversal(root.left)
        right = self.postorder_traversal(root.right)
        # 合併:
        result += left
        result += right
        result.append(root.val)
        return result
