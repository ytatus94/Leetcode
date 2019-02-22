# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # divide conquer
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         paths = []
        
#         # 出口
#         if root is None:
#             return paths
        
#         # 因為有個 -> 符號，所以要考慮是葉子節點的特殊情況
#         if root.left is None and root.right is None:
#             paths.append(str(root.val))
        
#         # 拆解
#         left_paths = self.binaryTreePaths(root.left)
#         right_paths = self.binaryTreePaths(root.right)
        
#         for path in left_paths:
#             paths.append(str(root.val) + '->' + path)
#         for path in right_paths:
#             paths.append(str(root.val) + '->' + path)

#         return paths

    # traverse
    def binaryTreePaths(self, root):
        paths = []
        if root is None:
            return paths
        self.traverse(root, str(root.val), paths)
        return paths
    
    def traverse(self, root, curr_path, paths):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            paths.append(curr_path)
            return
        
        if root.left != None:
            self.traverse(root.left, curr_path + '->' + str(root.left.val), paths)
        if root.right != None:
            self.traverse(root.right, curr_path + '->' + str(root.right.val), paths)
            
# lintcode 480
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    # divide conquer
    # 傳回所有以 root 為根的所有路徑
    # def binaryTreePaths(self, root):
    #     # write your code here
    #     paths = []
    #     if root is None:
    #         return paths
            
    #     if root.left is None and root.right is None:
    #         return [str(root.val)]
            
    #     left_paths = self.binaryTreePaths(root.left)
    #     right_paths = self.binaryTreePaths(root.right)
        
    #     for left in left_paths: # 所有以 root.left 為根的路徑可能有好幾條
    #         paths.append(str(root.val) + '->' + left)
            
    #     for right in right_paths:
    #         paths.append(str(root.val) + '->' + right)
            
    #     return paths
        

    # traverse
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        
        path = []
        self.helper(root, result, path)
        return result
        
    def helper(self, root, result, path):
        if root.left is None and root.right is None:
            path.append(str(root.val))
            result.append('->'.join(path))
            return
       
        if root.left:
            self.helper(root.left, result, path + [str(root.val)])
            
        if root.right:
            self.helper(root.right, result, path + [str(root.val)])
