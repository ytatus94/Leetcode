# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一： divide conquer
# class Solution:
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         # 用 -1 表示非平衡 binary tree
#         # 如果不是 -1 就是平衡的
#         return self.max_depth(root) != -1
    
#     def max_depth(self, root):
#         # 出口
#         if root is None:
#             return 0
        
#         # 拆解
#         left = self.max_depth(root.left)
#         right = self.max_depth(root.right)
        
#         # 判斷是否是平衡 binary tree
#         # 左右子樹必須是平衡 binary tree
#         # 且左右子樹的高度差不可以超過 1
#         if left == -1 or right == -1 or abs(left-right) > 1:
#             return -1 # 其中一個不滿足，表示是非平衡的 binary tree，回傳 -1
        
#         # 如果是平衡的 binary tree 就回傳當節點的前高度
#         return max(left, right) + 1
    

# 方法二
# 因為要記錄是否是平衡的，還有最大深度，有兩個值要紀錄，所以要用 ResultType
class ResultType:
    isBalanced = False
    max_depth = -1
    def __init__(self, isBalanced, max_depth):
        self.isBalanced = isBalanced
        self.max_depth = max_depth
        
class Solution:
    def isBalanced(self, root):
        return self.helper(root).isBalanced
    
    def helper(self, root):
        if root is None:
            return ResultType(True, 0)
            
        # 拆解
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # 判斷左右子樹是否是平衡 binary tree
        if not left.isBalanced or not right.isBalanced:
            return ResultType(False, -1)
        
        # 判斷左右子樹的高度差是否 <= 1
        if abs(left.max_depth - right.max_depth) > 1:
            return ResultType(False, -1)
    
        # 如果上面的條件都通過了，表示當前以 root 為根的樹是平衡的
        return ResultType(True, max(left.max_depth, right.max_depth) + 1)

# 方法三: 利用 python 的函數可以傳回多個值的特性
# class Solution:
#     def isBalanced(self, root):
#         balanced, depth = self.helper(root)
#         return balanced
    
#     def helper(self, root):
#         # 出口
#         if root is None:
#             return True, 0
        
#         # 拆解
#         left_balanced, left_depth = self.helper(root.left)        
#         right_balanced, right_depth = self.helper(root.right)

#         if not left_balanced:
#             return False, 0 # 不平衡就不在意高度了，回傳 0 就好
#         if not right_balanced:
#             return False, 0
        
#         return abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1

# lintcode 93
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
    @return: True if this Binary tree is Balanced, or false.
    """
    # Traverse + divide conquer
    # def isBalanced(self, root):
    #     # write your code here
    #     self.balanced = True
    #     self.helper(root)
    #     return self.balanced
        
    # # 傳回 root 為根的子樹的高度
    # def helper(self, root):
    #     if root is None:
    #         return 0
        
    #     left_height = self.helper(root.left)
    #     right_height = self.helper(root.right)
        
    #     if abs(left_height - right_height) > 1:
    #         self.balanced = False
    #         return -1
    #     elif left_height == -1 or right_height == -1:
    #         self.balanced = False
    #         return -1
        
    #     return max(left_height, right_height) + 1
        
    # divide conquer
    def isBalanced(self, root):
        # write your code here
        balanced, height = self.helper(root)
        return balanced
        
    # 傳回以 root 為根的子樹是否是平衡二叉樹
    # 如果是平衡二叉樹，還要傳回當前的高度
    def helper(self, root):
        if root is None:
            return True, 0
            
        left_balanced, left_height = self.helper(root.left)
        right_balanced, right_height = self.helper(root.right)

        if not left_balanced or not right_balanced:
            return False, -1 # 不平衡時高度就不重要了，用 -1 代表就好
            
        if abs(left_height - right_height) > 1:
            return False, -1
            
        # 左子樹和右子樹高度差等於 1 仍然是平衡的
        # 所以要挑出較大者 + 1 才是當前高度
        return True, max(left_height, right_height) + 1
