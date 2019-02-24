# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        
        results = []
        queue = [root] # 把所有的起點放到 queue 中
        left_to_right = True # 用來控制要由左到右還是由右到左的順序
        
        # 不斷的從 while loop 中把 queue 中的東西彈出來
        while queue:
            curr_level = [] # 用來保存彈出來的節點
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val) # 把彈出來的節點的值放到目前這層的列表裡面
                if node.left: # 左右子樹非空的話，就塞入 queue 中
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if left_to_right:
                results.append(curr_level)
            else: # 如果是從右到左，那就要反轉 curr_level 的順序後才塞入 results
                results.append(list(reversed(curr_level)))
            
            left_to_right = not left_to_right
            
        return results

# lintcode 71
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        results =[]
        q = [root]
        left_to_right = True
        while q:
            curr_level = []
            for i in range(len(q)):
                node = q.pop(0)
                curr_level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                    
            if left_to_right:
                results.append(curr_level)
            else:
                reversed_curr_level = list(reversed(curr_level))
                results.append(reversed_curr_level)
            left_to_right = not left_to_right
            
        return results
