# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 定義: 傳回滿足 [L, R] 區間的樹的根節點
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        
        '''
        當根節點的值比 R 大時，只有在左子樹裡面才可能找到符合 [L, R] 區間的樹
        當根節點的值比 L 小時，只有在右子樹裡面才可能找到符合 [L, R] 區間的樹
        當根節點的值正好介於 L < 根 < R，那就左右子樹都要去找
        '''
        if root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
