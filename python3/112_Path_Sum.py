# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = False # 小本本
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.helper(root, sum) # traverse
        return self.result
        
    # 定義
    def helper(self, root, sum):
        # 出口
        if root is None:
            return
        print(root.val, sum)
        
        # 拆解
        # 處理葉子節點
        if root.left is None and root.right is None:
            if root.val == sum:
                self.result = True
            return
        
        self.helper(root.left, sum - root.val)
        self.helper(root.right, sum - root.val)
