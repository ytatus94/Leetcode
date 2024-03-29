# lintcode 597
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
    def findSubtree2(self, root):
        # write your code here
        self.node = None
        self.max_avg = float('-inf')
        self.helper(root)
        return self.node
        
    # return subtree sum and node counts
    def helper(self, root):
        if root is None:
            return 0, 0
            
        left_sum, left_counts = self.helper(root.left)
        right_sum , right_counts = self.helper(root.right)
        
        curr_sum = root.val + left_sum + right_sum
        curr_counts = 1 + left_counts + right_counts
        curr_avg = float(curr_sum) / curr_counts
        
        if curr_avg > self.max_avg:
            self.max_avg = curr_avg
            self.node = root
            
        return curr_sum, curr_counts

class Solution:
    # divide conquer
    def findSubtree2(self, root):
        node, sum, counts = self.helper(root)
        return node
        
    # 傳回以 root 為根的子樹中
    # 1. 平均值最大的子樹的根節點
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
    
from lintcode import (
    TreeNode,
)

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
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.node = None
        self.max_average = float("-inf")
        sum_of_nodes, num_of_nodes = self.helper(root)
        return self.node

    # 定義: 找出以 root 為根的子樹的和，還有節點數目
    def helper(self, root):
        # 出口:
        if root is None:
            return 0, 0
        # 拆解:
        left_sum, left_num = self.helper(root.left)
        right_sum, right_num = self.helper(root.right)

        current_sum = left_sum + right_sum + root.val
        current_num = left_num + right_num + 1

        # 打擂台
        if current_sum / current_num > self.max_average:
            self.max_average = current_sum / current_num
            self.node = root

        return current_sum, current_num

from lintcode import (
    TreeNode,
)

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
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        _, _, _, best_node = self.helper(root, float("-inf"), None)
        return best_node

    def helper(self, root, maximum_average, best_node):
        if root is None:
            return 0, 0, maximum_average, best_node

        left_sum, left_nodes, maximum_average, best_node = self.helper(root.left, maximum_average, best_node)
        right_sum, right_nodes, maximum_average, best_node = self.helper(root.right, maximum_average, best_node)

        current_sum = root.val + left_sum + right_sum
        current_nodes = 1 + left_nodes + right_nodes
        current_average = current_sum / current_nodes

        if current_average > maximum_average:
            maximum_average = current_average
            best_node = root

        return current_sum, current_nodes, maximum_average, best_node
