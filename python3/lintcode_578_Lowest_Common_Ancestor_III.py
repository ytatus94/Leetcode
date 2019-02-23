"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if root is None:
            return None
            
        a_exist = self.helper(root, A)
        b_exist = self.helper(root, B)
        
        if not a_exist or not b_exist:
            return None
            
        return self.lca(root, A, B)

    def helper(self, root, node):
        if root is None:
            return False
            
        if node == root:
            return True
            
        left = self.helper(root.left, node)
        right = self.helper(root.right, node)
        
        if left or right:
            return True
            
        return False
        
    def lca(self, root, A, B):
        if root is None:
            return None
        
        if A == root or B == root:
            return root
            
        left = self.lca(root.left, A, B)
        right = self.lca(root.right, A, B)
        
        if left is not None and right is not None:
            return root
            
        if left:
            return left
            
        if right:
            return right
