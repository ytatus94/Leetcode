# Binary tree level order traversal 是很標準的 BFS 要背熟
# 其他的題目的解法都可以從這個模板做修改得到


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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if root is None:
            return results
        
        # BFS 用 Queue
        # 步驟
        # 1. 把所有的起點放到 queue 裡面
        # 2. 用 while loop 不斷地從 queue 把節點 pop 出來
        # 3. 把 pop 出來的節點當作 head, 把 head 的下一層放到 queue 裡面
        
        queue = list()
        queue.append(root) # 1. 把所有的起點放到 queue 裡面
        
        while len(queue) > 0:
            current_level = [] # 每個 loop 就是新的一層
            size = len(queue) # 我覺得先算出 size 比較好，這樣才不會因為 queue.append() 而改變長度 (雖然好像長度不會改變，先算出 size 比較保險)
            for node in range(size):
                head = queue.pop(0) # 2. 從 queue 把節點 pop 出來
                current_level.append(head.val) # 把這一層的東西加進去
                if head.left is not None:
                    queue.append(head.left) # 把下一層的放到 queue 裡面
                if head.right is not None:
                    queue.append(head.right) # 把下一層的放到 queue 裡面
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
