class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # traverse
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        # 出口:
        if root is None:
            return
        # 拆解
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)

    # divide conquer (32ms)
#     def postorderTraversal(self, root):
#         result = []
#         # 出口:
#         if root is None:
#             return result
#         # 拆解:
#         left = self.postorderTraversal(root.left)
#         right = self.postorderTraversal(root.right)
#         # 合併:
#         result = result + left
#         result = result + right
#         result.append(root.val)
        
#         return result

# lintcode 68
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
    @return: Postorder in ArrayList which contains node values.
    """
    # divide conquer
    # def postorderTraversal(self, root):
    #     # write your code here
    #     result = []
    #     if root is None:
    #         return result
            
    #     left = self.postorderTraversal(root.left)
    #     right = self.postorderTraversal(root.right)
        
    #     result = result + left
    #     result = result + right
    #     result.append(root.val)
        
    #     return result
    
    # traverse
    # def postorderTraversal(self, root):
    #     result = []
    #     self.helper(root, result)
    #     return result
        
    # def helper(self, root, result):
    #     if root is None:
    #         return
        
    #     self.helper(root.left, result)
    #     self.helper(root.right, result)
    #     result.append(root.val)
    
    # Non-recurssion
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
            
        prev = None
        node = root
        
        stack = [root]
        while stack:
            node = stack[-1]
            if prev is None or prev.left == node or prev.right == node:
                # print(node.val)
                if node.left is not None:
                    stack.append(node.left)
                elif node.right is not None:
                    stack.append(node.right)
            elif node.left == prev:
                if node.right is not None:
                    stack.append(node.right)
            else:
                result.append(node.val)
                stack.pop()
            prev = node
            
        return result
