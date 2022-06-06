# lintcode 376
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    # Traverse
    def binaryTreePathSum(self, root, target):
        # write your code here
        result = []
        if root is None:
            return result
            
        paths = []
        paths.append(root.val)
        self.helper(root, paths, root.val, target, result)
        return result
        
    def helper(self, root, paths, sum, target, result):
        # 出口: 處理葉子節點
        if root.left is None and root.right is None:
            if sum == target:
                result.append(paths[:]) # 注意要用 deep copy
            return
        
        # 拆解
        if root.left is not None:
            paths.append(root.left.val)
            self.helper(root.left, paths, sum + root.left.val, target, result)
            paths.pop()
            
        if root.right is not None:
            paths.append(root.right.val)
            self.helper(root.right, paths, sum + root.right.val, target, result)
            paths.pop()

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
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        results = []
        # 可以選擇要傳入的 current_path 和 current_sum 是要用
        # root.val 傳入還是要用空傳入，如果要用 root.val 傳入，
        # 就要先檢查 root 是不是空
        if root is None: 
            return results
        current_path = [root.val] 
        current_sum = root.val
        self.helper(root, current_path, current_sum, target, results)
        return results

    # 定義: 傳回以 root 為根的所有路徑，且路徑和等於 target
    # 因為要找 "所有" --> 用 DFS
    # 這一題基本上就和 subset 一樣，只是輸入的資料是 binary tree 的結構而已
    def helper(self, root, current_path, current_sum, target, results):
        if root is None:
            return

        if root.left is None and root.right is None and current_sum == target:
            results.append(current_path.copy()) # 記住 subset 類型的題目都要 deep copy
            return
        
        # 有可能左右子樹其中一個是空，所以要先檢查是不是空，不然 .val 會出錯
        if root.left is not None:
            self.helper(root.left, current_path + [root.left.val], current_sum + root.left.val, target, results)
            
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
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        results = []
        # 如果 current_path 和 current_sum 用空傳入的話
        current_path = []
        current_sum = 0
        self.dfs(root, current_path, current_sum, target, results)
        return results

    # 定義: 把以 root 為根，且路徑和等於 target 的路徑放到 results 裡面去
    def dfs(self, root, current_path, current_sum, target, results):
        # 出口:
        if root is None:
            return
        # 如果最初 current_path 用空傳入，那要在這邊加入 root.val
        current_path.append(root.val)
        current_sum += root.val
        # 當葉子節點的時候，要比較當前的和
        if root.left is None and root.right is None: # 葉子節點時
            if current_sum == target:
                # 當路徑和等於 target 時就要把 current_path 放到 results 裡面去
                # 而且再放入的時候要用 deep copy
                results.append(current_path[:])

        # 因為最初是用 current_path = [] 和 current_sum = 0 傳入的
        # 所以這邊傳入 current_path 和 current_sum 時，只和當前 root 的資訊有關
        # 和子樹的資訊無關，因此不論子樹是不是空都沒關係，不需要事先檢查
        self.dfs(root.left, current_path, current_sum, target, results)
        self.dfs(root.right, current_path, current_sum, target, results)
        # 但是這種方式就要注意要 pop 最後一個，這樣回到上一層的呼叫的時候
        # 上一層的 current_path 才不會有問題
        # 畢竟上一層的 current_path 並不包括 root.val
        current_path.pop()

        
        if root.right is not None:
            self.helper(root.right, current_path + [root.right.val], current_sum + root.right.val, target, results)

        
