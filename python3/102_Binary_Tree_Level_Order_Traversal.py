# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Binary tree 是一種圖，圖的遍歷用 BFS
        # 要先檢查 root 是不是空
        if not root:
            return []

        # 1. 把所有的起點放到 queue 裡面
        queue = [root]
        results = []
        
        # 2. while 循環，不斷的從 queue 中 pop 出節點
        while queue:
            current_level = []
            for i in range(len(queue)):
                node = queue.pop(0) # pop() 預設是 pop 最後一個，queue 是先進先出，所以要指定 index
                current_level.append(node.val)
                # 3. 把 node 下一層的節點放到 queue 中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(current_level)
        
        return results

# lintcode 69
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        results = []
        if root is None:
            return results
        
        queue = [root]

        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(curr_level)
            
        return results
