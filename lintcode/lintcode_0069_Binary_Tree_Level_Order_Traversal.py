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

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here

        # Binary tree 是一種圖，圖的遍歷用 BFS
        # BSF: 
        # * 適用於: 層級遍歷，由點及面，拓樸排序，簡單圖的最短路徑
        # * 用 queue
        # * 步驟:
        #   1. 把所有的起點放到 queue 裡面
        #   2. 用 while loop 不斷地從 queue 把節點 pop 出來
        #   3. 把 pop 出來的節點當作 head, 把 head 的下一層放到 queue 裡面

        if root is None:
            return []

        results = []
        
        # 1. 把所有的起點放到 queue 裡面
        queue = [root]
        # 2. 用 while loop 不斷地從 queue 把節點 pop 出來
        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                current_level.append(node.val)
                # 3. 把 pop 出來的節點當作 head, 把 head 的下一層放到 queue 裡面
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            results.append(current_level)
        return results
