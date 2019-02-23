# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        if root is None:
            return self.count
        
        # 算以 root 為根的子樹中有多少個 path 滿足 sum 的要求
        # 可是題目說起點不一定要從 root 開始 所以從左右子樹開始的起點
        # 如果滿足要求的話，也要納入結果
        self.count = self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
        return self.count
        
    # 定義: 傳回以 root 為根的子樹中有多少個 path 滿足 path sum 的要求
    def helper(self, root, sum):
        # 出口
        if root is None:
            return 0
        
        # 拆解
        left_count = self.helper(root.left, sum - root.val)
        right_count = self.helper(root.right, sum - root.val)
        
        count = left_count + right_count
        
        # root 本身的值如果和 sum 一樣時，也要考慮進去
        if root.val == sum:
            return count + 1
        
        return count
