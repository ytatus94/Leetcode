# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 方法一: Traverse (32ms)
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
         
        result = []
        self.traverse(root, result)
        return result

    # 定義: 傳回以 root 為根的遍歷的結果
    def traverse(self, root, result):
        # 出口: 處理空節點
        if root is None:
            return
        
        # 拆解
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)

class Solution:     
    # 方法二: divide conquer
    def preorderTraversal(self, root):
        result = []

        # 出口: 處理空節點
        if root is None:
            return result
        
        # 拆解 (分): 先無腦的處理左右子樹
        left_tree = self.preorderTraversal(root.left)
        right_tree = self.preorderTraversal(root.right)
        
        # 合併：
        result.append(root.val)
        result = result + left_tree
        result = result + right_tree
        
        return result
        
# lintcode 66
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    # divide conquer
    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
            
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        result.append(root.val)
        result = result + left
        result = result + right
        
        return result

class Solution:
    # traverse
    def preorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        if root is None:
            return
        
        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)

class Solution:
    # Non recursion
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
            
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            # stack 後進先出，所以右子樹要先加入，再加入左子樹
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
