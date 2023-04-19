"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {int} an integer
    def leafSum(self, root):
        # Write your code here
        result = []
        self.dfs(root, result)
        return sum(result)

    def dfs(self, root, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(root.val)

        self.dfs(root.left, result)
        self.dfs(root.right, result)
