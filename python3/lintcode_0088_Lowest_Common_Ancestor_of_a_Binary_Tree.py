"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    # 定義: 在以 root 為根的子樹中找出 A 或 B
    # 如果有找到 A 就傳回 A
    # 如果有找到 B 就傳回 B
    # 如果找不到就傳回 None
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        # 會有下列幾種情況
        # 1. root 是 A 或 root 是 B，這時候 LCA = root
        # 2. A 是 B 的祖先，則 LCA = A
        # 3. B 是 A 的祖先，則 LCA = B
        # 4. A 和 B 分別在 root 左子樹和右子樹中 (一邊一個)，則 LCA = root
        # 5. 找不到

        # 出口:
        if root is None:
            return None
        
        if root == A or root == B:
            return root # 情形 1

        left_side = self.lowestCommonAncestor(root.left, A, B)
        right_side = self.lowestCommonAncestor(root.right, A, B)

        if left_side is not None and right_side is not None:
            return root # 情形 4
        if left_side is not None and right_side is None:
            return left_side # 情形 2 或情形 3
        if left_side is None and right_side is not None:
            return right_side # 情形 2 或情形 3

        return None
