# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 先把兩棵樹都平坦化，然後比較平坦化的結果
        # 平坦化可以用 traversal, divid conquer, BFS, DFS
        
        # 用 traversal 平坦化，因為 traversal 不回傳東西，所以要把 results 當參數傳遞
        r1 = []
        self.traversal(r1, p)

        r2 = []
        self.traversal(r2, q)

        if r1 == r2:
            return True
        else:
            return False

    def traversal(self, results, root):
        if root is None:
            return
        
        results.append(root.val)
        if root.left:
            self.traversal(results, root.left)
        else:
            results.append("#") # 考慮到可能有一邊是空的

        if root.right:
            self.traversal(results, root.right)
        else:
            results.append("#") # 考慮到可能有一邊是空的
            
# 方法 2: 用 divide conquer 來平坦化，會比 traversal 慢

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_p = self.helper(p)
        tree_q = self.helper(q)

        if tree_p == tree_q:
            return True
        else:
            return False

    def helper(self, root):
        if root is None:
            return

        left_result = self.helper(root.left)
        right_result = self.helper(root.right)

        results = [root.val]
        if left_result is not None:
            results += left_result
        else:
            results += ["#"]
        if right_result is not None:
            results += right_result
        else:
            results += ["#"]
        return results
