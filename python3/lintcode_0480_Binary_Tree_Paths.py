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

# 用 Traverse 的方法
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        result = []
        if root is None:
            return result
        # 因為 root.val 是數值，要記得轉成字串才能和 -> 結合
        current_path = str(root.val)
        self.dfs(root, current_path, result)
        return result

    # 定義: 把從 root 出發的所有路徑放到 result
    # 找出所有方案==>用深度優先搜索 DFS
    # 這邊用 traversal 來實現 DFS，所以需要一個 current＿path 來保存當前路徑
    def dfs(self, root, current_path, result):
        # 出口: 處理空節點
        # 遇到空節點就什麼都不做，直接回傳
        if root is None:
            return
        # 當遇到葉子節點的時候，就把現在累積起來的路徑放到 result 裡面，然後回傳
        if root.left is None and root.right is None:
            result += [current_path]
            return
        # 拆解:
        if root.left is not None:
            self.dfs(root.left, current_path + "->" + str(root.left.val) , result)
        if root.right is not None:
            self.dfs(root.right, current_path + "->" + str(root.right.val), result)

# 用 Divide conquer 的方法
# 用 Traverse 的方法
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    定義: 求出從 root 出發的所有路徑
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        # 找出所有方案==>用深度優先搜索 DFS
        # 因為題目是 binary tree 所以用二叉樹上的深度優先搜索
        result = []
        # 出口: 處理空節點
        # 遇到空節點就什麼都不做，直接回傳
        if root is None:
            return result
        # 但是當葉子節點時，不會有要加上 -> 的情形，所以需要特別處理一下葉子節點
        if root.left is None and root.right is None:
            result += [str(root.val)]
            return result
        # 拆解:
        left_path = self.binary_tree_paths(root.left)
        right_path = self.binary_tree_paths(root.right)
        # 合併:
        for path in left_path:
            result += [str(root.val) + "->" + path]
        for path in right_path:
            result += [str(root.val) + "->" + path]

        return result
