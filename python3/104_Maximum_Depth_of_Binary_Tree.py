# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     depth = 0 # 要每個函數都能看到 depth 所以要放在函數外面
    
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # traverse (76ms)
#         self.traverse(root, 1) # root 當前深度是 1
#         return self.depth
        
#     def traverse(self, root, curr_depth):
#         # 出口
#         if root is None:
#             return
#
#         if self.depth < curr_depth:
#             self.depth = curr_depth
#         # 拆解
#         self.traverse(root.left, curr_depth + 1) # +1 是加上目前這層
#         self.traverse(root.right, curr_depth + 1)

    # divide conquer
    def maxDepth(self, root):
        depth = 0
        # 出口
        if root is None:
            return depth
        
        # 拆解
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1 # +1 是因為 root 那層
        
# lintcode 97
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # divide conquer
    # 傳回以 root 為根的子樹的最大深度
    # def maxDepth(self, root):
    #     # write your code here
    #     if root is None:
    #         return 0
            
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)

    #     max_depth = 1 + max(left, right)
        
    #     return max_depth
    
    # traverse
    def maxDepth(self, root):
        self.max_depth = 0
        self.helper(root, 1) # 目前這層深度是 1
        return self.max_depth
        
    def helper(self, root, depth):
        if root is None:
            return
        
        if depth > self.max_depth:
            self.max_depth = depth
        
        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)
