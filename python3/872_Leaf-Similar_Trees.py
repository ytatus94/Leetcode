# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        
        # 當 root1 和 root2 都不是空
        leaf1 = self.get_leafs(root1)
        leaf2 = self.get_leafs(root2)
        print(leaf1)
        print(leaf2)
        
        if leaf1 == leaf2:
            return True
        return False
    
    # 定義: 傳回以 root 為根的所有葉子節點
    def get_leafs(self, root):
        result = []
        if root is None:
            return result
        
        left = self.get_leafs(root.left)
        right = self.get_leafs(root.right)
        
        if len(left) == 0 and len(right) == 0:
            result.append(root.val)
        else:
            result += left
            result += right

        return result
