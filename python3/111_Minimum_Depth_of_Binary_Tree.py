# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # divide conquer
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        # 出口
        if root is None:
            return depth

        # 拆解
        # 有三種情況
        left, right = 0, 0

        # 1. 右子樹為空，只有左子樹時，傳回左子樹的最小深度
        if root.right is None and root.left != None:
            left = self.minDepth(root.left) + 1
            return left
        
        # 2. 左子樹為空，只有右子樹時，傳回右子樹的最小深度
        if root.left is None and root.right != None:
            right = self.minDepth(root.right) + 1
            return right
        
        # 3. 左右子樹都不為空，傳回左右子樹兩者中的最小深度
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        return min(left, right) + 1 # +1 是因為要加上當前節點
   
# lintcode 155
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
            
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left == 0:
            return 1 + right
        elif right == 0:
            return 1 + left
        else:
            return 1 + min(left, right)
