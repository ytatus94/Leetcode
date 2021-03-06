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

class Solution:
    # divide conquer (76ms)
    def inorderTraversal(self, root):
        result = []
        # 出口:
        if root is None:
            return result
        
        # 分: 無腦調用左右子樹
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        # 合:
        result = result + left
        result.append(root.val)
        result = result + right

        return result

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
    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
            
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        result = result + left
        result.append(root.val)
        result = result + right

        return result

class Solution:
    # traverse
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        if root is None:
            return
        
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)

# Non-recursion 版本
class Solution:
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

# Non-recursion 版本
class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        curr = root
        while curr or stack:
            # 一路把最左邊都塞到 stack 裡面
            while curr:
                stack.append(curr)
                curr = curr.left
            # 從 stack pop 出最後一個，把它加入 result 裡面
            # 然後移動到它的右子樹
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
                
