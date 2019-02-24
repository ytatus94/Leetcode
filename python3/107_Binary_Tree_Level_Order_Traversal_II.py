# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 層級遍歷用 BFS
        self.result = []
        
        if root is None:
            return self.result
        
        # 把所有的起點放到 queue
        queue = [root]
        # 用 while loop 不斷的把 queue 中的東西 pop 出來
        while queue:
            # queue 裡面只是放某一層的
            # 所以要先把目前這一層的節點放入 result 中
            self.result.append([node.val for node in queue])
            
            # 用目前這一層的節點來找下一層的節點
            new_queue = [] # 用來存放下一層的節點
            for n in queue:
                if n.left:
                    new_queue.append(n.left)
                if n.right:
                    new_queue.append(n.right)
                    
            # 再把目前這層改成下一層
            queue = new_queue
            
        # 所以當離開回圈時 result 就存放了每一層的節點，由 root 到 leaf
        # 因此要把順序顛倒過來 (用 reversed，但是 reversed 不傳回 list)
        return list(reversed(self.result))

# lintcode 70
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
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
            
        return list(reversed(results))
