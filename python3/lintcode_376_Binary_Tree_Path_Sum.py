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
