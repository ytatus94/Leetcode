# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        paths = []
        
        if root is None:
            return result
        
        self.helper(root, sum, paths, result)
        return result

    def helper(self, root, sum, paths, result):
        if root is None:
            return
        
        # 把當前節點放到 path 中
        # 最後 path 要不要放入 result 是看葉子節點來決定
        curr_path = paths + [root.val]
            
        # 跑到葉子節點時，如果剛好 root.val 和 sum 一樣，表示這整個 path sum 是正確的
        # 要放到 result 裡面
        if root.left is None and root.right is None:
            if root.val == sum:
                result.append(curr_path)
            return
        
        # 拆解
        self.helper(root.left, sum - root.val, curr_path, result)
        self.helper(root.right, sum - root.val, curr_path, result)
