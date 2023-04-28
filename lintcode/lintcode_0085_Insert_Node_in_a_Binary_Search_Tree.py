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
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        if root.val < node.val: # 往右子樹內插入
            root.right = self.insertNode(root.right, node)
        else: # root.val > node.val 時往左子樹內插入
            root.left = self.insertNode(root.left, node)

        return root
