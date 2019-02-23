# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # BST 要求左子樹的每一個點都比根節點小，右子樹的每一個點都比根節點大
        # 如果插入的值比根節點小，就插到左子樹
        # 如果插入的值比根節點大，就插到右子樹
        node = TreeNode(val)
        
        if root is None:
            return node # root 是空的時候，node 變成根節點
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        
# lintcode 85
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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    # 樹的結構發生了變化，只能用 divide conquer
    def insertNode(self, root, node):
        # write your code here
        if root is None and node is None:
            return None
        
        if root is None and node is not None:
            return node
        
        if node.val < root.val: # 往左子樹中插入
            left = self.insertNode(root.left, node)
            root.left = left
        
        if node.val > root.val: # 往右子樹中插入
            right = self.insertNode(root.right, node)
            root.right = right
            
        return root
