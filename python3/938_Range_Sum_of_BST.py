# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # BST 的左子樹一定比根節點小，右子樹一定比根節點大
        if root is None:
            return 0
        # 如果 L 比根節點大，就往右子樹看
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        # 如果 R 比根節點小，就往左子樹看
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        
        left = self.rangeSumBST(root.left, L, R)
        right = self.rangeSumBST(root.right, L, R)
        
        return root.val + left + right
