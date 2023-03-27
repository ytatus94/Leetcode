# Binary tree level order traversal i 和 Binary tree level order traversal ii 做法一模一樣
# 只是在 ii 中，最後要傳回的時候要 reverse 一下
#
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        results = []
        if root is None:
            return results

        queue = [root]
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(curr_level)
            
        return list(reversed(results))

# 方法 2:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []

        results = []
        queue = [root] # 把所有的起點加到 queue 中
        while queue:
            # 把現在這一層所有的點加入到 results
            curr_layer = [node.val for node in queue]
            results.append(curr_layer)
            # 把下一層加入到 queue 中
            next_layer = []
            for node in queue:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            queue = next_layer

        return list(reversed(results))
