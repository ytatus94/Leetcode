# lintcode 596
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
    @return: the root of the minimum subtree
    """
    # Traverse + divide conquer
    findSubtree() 本身用的是 Traverse
    def findSubtree(self, root):
        # write your code here
        self.minimum = float('inf') # 要記錄當前 subtree sum 的最小值
        self.subtree = None # 紀錄是哪一個節點有最小的 subtree sum
        self.helper(root)
        return self.subtree
     
    # helper() 本身是 divide conquer，用來計算和傳回 minimum of the subtree sum
    def helper(self, node):
        if node is None:
            return 0
        
        # divide conquer
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        subtree_sum = node.val + left + right
        
        if subtree_sum < self.minimum:
            self.minimum = subtree_sum
            self.subtree = node
            
        return subtree_sum

class Solution:
    # divide conquer
    def findSubtree(self, root):
        subtree, minimum, sum = self.helper(root)
        return subtree
        
    # 傳回以 root 為根的子樹的
    # 1. 節點的和
    # 2. 節點的和的最小值
    # 3. 最小和的子樹
    def helper(self, root):
        if root is None:
            return None, sys.maxsize, 0
            
        left_node, left_min, left_sum = self.helper(root.left)
        right_node, right_min, right_sum = self.helper(root.right)
        
        curr_sum = root.val + left_sum + right_sum
        curr_min = min(curr_sum, left_min, right_min)
        
        if left_min == curr_min:
            return left_node, curr_min, curr_sum
        if right_min == curr_min:
            return right_node, curr_min, curr_sum
        return root, curr_min, curr_sum

    
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
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.min_sum = float("inf")
        self.min_sum_node = None
        self.helper(root)
        return self.min_sum_node

    # 定義: 傳回以 root 為根的子樹的 sum
    def helper(self, root):
        # 出口:
        if root is None:
            return 0
        
        # 拆解:
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        current_sum = root.val + left_sum + right_sum

        # 打擂台
        if current_sum < self.min_sum:
            self.min_sum = current_sum
            self.min_sum_node = root

        return current_sum
