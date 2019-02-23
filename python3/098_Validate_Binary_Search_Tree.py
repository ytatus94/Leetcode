# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        is_bst, min_val, max_val = self.helper(root)
        return is_bst
    
    def helper(self, root):
        if root is None:
            return True, float('-inf'), float('inf')
        
        left_bst, left_min, left_max = self.helper(root.left)
        right_bst, right_min, right_max = self.helper(root.right)
        
        if not left_bst or not right_bst:
            return False, 0, 0
        
        # root 是葉子節點時
        if root.left is None and root.right is None:
            return True, root.val, root.val
        elif root.right is None:
            if left_max < root.val:
                return True, left_min, root.val
        elif root.left is None:
            if right_min > root.val:
                return True, root.val, right_max
        else:
            if left_max < root.val and root.val < right_min:
                return True, left_min, right_max
            
        return False, 0, 0

class Solution:
     def isValidBST(self, root):
         self.is_BST = True
         self.last_val = None
         self.helper(root)
         return self.is_BST
        
     def helper(self, root):
         if root is None:
             return
            
         # BST 是 in-order 左根右
         self.helper(root.left)
         # 根
         # 因為 in-order 所以左子樹最後一個點的最大值會是整個子樹的最大值
         if self.last_val is not None and self.last_val >= root.val:
             self.is_BST = False
             return
         self.last_val = root.val
        
         self.helper(root.right)

# lintcode 95
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
    @return: True if the binary tree is BST, or false
    """
    # divide conquer
    # def isValidBST(self, root):
    #     # write your code here
    #     is_BST, min_val, max_val = self.helper(root)
    #     return is_BST
        
    # # 傳回以 root 為根的子樹
    # # 1. 是否是 BST
    # # 2. 節點的最小值
    # # 3. 節點的最大值
    # def helper(self, root):
    #     if root is None: # 空節點算是 BST
    #         return True, -1 * sys.maxsize, sys.maxsize
            
    #     left_BST, left_min, left_max = self.helper(root.left)
    #     right_BST, right_min, right_max = self.helper(root.right)
        
    #     if not left_BST or not right_BST:
    #         return False, 0, 0 # 只要一邊不是 BST 就回傳 Fasle 此時 min, max 已經不重要了，用 0 就好
            
    #     # 當左右子樹都是 BST 時仍然要和 root 比較才知道是否整棵樹是 BST
    #     # 因為空節點，或是只有一個節點時，都會被判斷成 BST
    #     # 所以又分成了 3 種情形
    #     # 1. root 是葉子節點
    #     # 2. 只有左子樹或只有右子樹
    #     # 3. 左右子樹都存在
    #     if root.left is None and root.right is None:
    #         return True, root.val, root.val
    #     elif root.right is None: # 只有左子樹
    #         if left_max < root.val:
    #             return True, left_min, root.val
    #     elif root.left is None: # 只有右子樹
    #         if root.val < right_min:
    #             return True, root.val, right_max
    #     else: # 左右子樹都不空
    #         if left_max < root.val and root.val < right_min:
    #             return True, left_min, right_max
                
    #     return False, 0, 0
    
    # traverse
    def isValidBST(self, root):
        self.is_BST = True
        self.last_val = None
        self.helper(root)
        return self.is_BST
        
    def helper(self, root):
        if root is None:
            return
            
        # BST 是 in-order 左根右
        self.helper(root.left)
        # 根
        # 因為 in-order 所以左子樹最後一個點的最大值會是整個子樹的最大值
        if self.last_val is not None and self.last_val >= root.val:
            self.is_BST = False
            return
        self.last_val = root.val
        
        self.helper(root.right)
