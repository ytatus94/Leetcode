# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        # stack 是後進先出，BST 左子樹都比根節點小，所以一直把左邊塞入 stack
        # 就會是大的先進去，彈出來的時候就是由小到大
        # 只塞左子樹就好，右子樹在 next() 中處理
        while root is not None:
            self.stack.append(root)
            root = root.left
    
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop() # 把目前 stack 中最後一個彈出來
        x = node.right # node 的右邊 (可能是右子樹，也可能是空)
        while x: # node 有右子樹，就要把右子樹加入 stack
            self.stack.append(x)
            # BST 是 inorder，塞入 x 後要把 x 的左子樹的左半邊一路塞到底
            # 彈出時才會是正確的順序
            x = x.left
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# lintcode 86
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        # 塞入最左邊的樹就好
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node
