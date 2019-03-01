# lintcode 011
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    # traverse
    def searchRange(self, root, k1, k2):
        # write your code here
        self.result = []
        self.helper(root, k1, k2)
        return self.result
        
    def helper(self, root, k1, k2):
        if root is None:
            return None
            
        self.helper(root.left, k1, k2)
        if k1 <= root.val and root.val <= k2:
            self.result.append(root.val)
        self.helper(root.right, k1, k2)

class Solution:   
    # divide conquer
    def searchRange(self, root, k1, k2):
        if root is None:
            return []
            
        result = []
        left = self.searchRange(root.left, k1, k2)
        right = self.searchRange(root.right, k1, k2)
        
        result += left
        if k1 <= root.val and root.val <= k2:
            result += [root.val]
        result += right
        
        return result
