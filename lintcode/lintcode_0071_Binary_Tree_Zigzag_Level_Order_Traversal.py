# Binary Tree Zigzag Level Order Traversal  和 Binary Tree Level Order Traversal 的差別在於
# zigzag level order traversal 是找出 current level 的點之後，要先把 current level 反轉之後再放入 result 裡面
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []

        results = []
        queue = [root] # 把所有的起點放到 queue 裡面
        layer_number = 0 # 用來記錄第幾層，奇數層就要反轉順序，偶數層就不用
        while queue:
            # 把現在這一層的所有點，加入到 results
            curr_layer = [node.val for node in queue]
            # 是否需要反轉？
            if layer_number %2 != 0:
                curr_layer = list(reversed(curr_layer))
            # 反轉必須要對 curr_layer 做，如果是對 next_layer 做
            # 那 next_layer 的下一層順序也會被反轉，因為 for loop 中是先放了左子樹再放右子樹
            results.append(curr_layer)
            # 把下一層的所有點，加入到 queue
            next_layer = []
            layer_number += 1
            print(layer_number)
            for node in queue:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            queue = next_layer

        return results

# 方法 2:
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []

        results = []
        queue = [root]
        reverse_layer = False

        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            if reverse_layer:
                reversed_current_level = list(reversed(current_level))
                results.append(reversed_current_level)
            else:
                results.append(current_level)
            reverse_layer = not reverse_layer
        return results
