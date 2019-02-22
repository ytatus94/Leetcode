class Solution:
    # traverse
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = [] # 小本本
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        # 出口:
        if root is None:
            return

        # 拆解:
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
    
#     # divide conquer (76ms)
#     def inorderTraversal(self, root):
#         result = []
#         # 出口:
#         if root is None:
#             return result
        
#         # 分: 無腦調用左右子樹
#         left = self.inorderTraversal(root.left)
#         right = self.inorderTraversal(root.right)
        
#         # 合:
#         result = result + left
#         result.append(root.val)
#         result = result + right

#         return result

# lintcode 67
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
    @return: Inorder in ArrayList which contains node values.
    """
    # divide conquer
    # def inorderTraversal(self, root):
    #     # write your code here
    #     result = []
    #     if root is None:
    #         return result
            
    #     left = self.inorderTraversal(root.left)
    #     right = self.inorderTraversal(root.right)
        
    #     result = result + left
    #     result.append(root.val)
    #     result = result + right

    #     return result
        
    # traverse
    # def inorderTraversal(self, root):
    #     result = []
    #     self.helper(root, result)
    #     return result
        
    # def helper(self, root, result):
    #     if root is None:
    #         return
        
    #     self.helper(root.left, result)
    #     result.append(root.val)
    #     self.helper(root.right, result)
    
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
            
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                result.append(stack[-1].val)
        return result
