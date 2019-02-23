"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # Traverse + divide conquer
    # def findSubtree2(self, root):
    #     # write your code here
    #     self.node = None
    #     self.max_avg = float('-inf')
    #     self.helper(root)
    #     return self.node
        
    # # return subtree sum and node counts
    # def helper(self, root):
    #     if root is None:
    #         return 0, 0
            
    #     left_sum, left_counts = self.helper(root.left)
    #     right_sum , right_counts = self.helper(root.right)
        
    #     curr_sum = root.val + left_sum + right_sum
    #     curr_counts = 1 + left_counts + right_counts
    #     curr_avg = float(curr_sum) / curr_counts
        
    #     if curr_avg > self.max_avg:
    #         self.max_avg = curr_avg
    #         self.node = root
            
    #     return curr_sum, curr_counts
        
    # divide conquer
    def findSubtree2(self, root):
        node, sum, counts = self.helper(root)
        return node
        
    # 傳回以 root 為根的子樹中
    # 1. 平均值最大的子數的根節點
    # 2. 子樹的和
    # 3. 子樹的節點數目
    def helper(self, root):
        if root is None:
            return None, 0, 0
            
        left_node, left_sum, left_counts = self.helper(root.left)
        right_node, right_sum, right_counts = self.helper(root.right)
        
        curr_sum = root.val + left_sum + right_sum
        curr_counts = 1 + left_counts + right_counts

        # 一直有問題跑不出正確答案
        curr_avg = float(curr_sum) / curr_counts
        # left_avg, right_avg = 0, 0
        left_avg, right_avg = -1 * sys.maxsize, -1 * sys.maxsize
        if left_counts > 0:
            left_avg = float(left_sum) / left_counts
        if right_counts > 0:
            right_avg = float(right_sum) / right_counts

        if left_avg > right_avg and left_avg > curr_avg:
                return left_node, left_sum, left_counts
        if right_avg > left_avg and right_avg > curr_avg:
            return right_node, right_sum, right_counts
        
        return root, curr_sum, curr_counts
