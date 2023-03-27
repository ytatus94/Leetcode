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
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum2(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        results = []
        current_path = []
        self.dfs(root, target, current_path, results)
        return results

    # 定義: 把以 root 為根的路徑，且和等於 target 的路徑，放到 results 裡面去
    def dfs(self, root, target, current_path, results):
        # 出口:
        if root is None:
            return
        # 把當前節點加入到 current_path
        current_path.append(root.val)
        # 然後要檢查是否有以 root 結束的路徑剛好符合路徑和等於 target 的
        # 在 current_path 中的每個數都是 binary tree 中不同的層
        # 和 376. Binary Tree Path Sum 不同的地方是，這裡要考慮任一節點開始，到任一節點結束的路徑和
        # 所以判斷的時候就不需要用葉子節點，而是以當前 root 節點為結束路徑的就要考慮
        sum_of_path = 0
        path = []
        print(current_path)
        for node_val in current_path[::-1]: 
            sum_of_path += node_val
            path.append(node_val)
            if sum_of_path == target:
                correct_path = path[::-1]
                results.append(correct_path[:])
        
        self.dfs(root.left, target, current_path, results)
        self.dfs(root.right, target, current_path, results)

        current_path.pop() # 要記得把 root.val 拿掉，這樣回傳到上一層的時候才不會出錯
