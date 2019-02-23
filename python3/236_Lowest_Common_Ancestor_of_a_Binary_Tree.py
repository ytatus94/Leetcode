# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # p, q 的分佈有幾種情形
        # 1. p 或 q 其中一個是 root
        # 2. p, q 一邊一個
        # 3. p, q 在同一邊
        # 4. 什麼都沒有 (因為 p, q 在同一邊，另一邊就什麼都沒有)
        
        # 1. p 或 q 其中一個是 root
        if root is None or p == root or q == root:
            return root
        
        # 先無腦的用 divide conquer 分別求左右子樹的
        # 判斷 p 或 q 是否在該子樹裡面
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 在子樹裡面 p, q 的存在與否，關係到回傳哪個
        # p & q => lca
        # !p & !q => null
        # p & !q => p 
        # !p & q => q
        if left is not None and right is not None:
            return root # root 是 lca
        
        # 左子樹或右子樹只存在其中一個時，把存在的那個回傳
        if left is not None:
            return left
        
        if right is not None:
            return right
        
        return None
        
# lintcode 88
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    # divide conquer
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
            
        if A == root or B == root:
            return root
            
        # A, B 有找到誰就回傳誰，要是兩個都找到就回傳 root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left is not None and right is not None:
            return root
        
        if left is not None:
            return left
            
        if right is not None:
            return right
        
        return None
