# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    last_node = None
    
    # traverse
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 用 divide conquer 的想法：
        # 先各自把左右子樹 flatten (用前序遍歷)
        # 再把 根節點 + 左子樹的前序遍歷 flatten + 右子樹的前序遍歷 flatten 接起來
        # 但是左子樹的 flatten 是要接到 root 的右邊
        # 右子樹的 flatten 要接到左子樹的 flatten 的最後一點
        # 所以要記錄上一層的最後一個節點

        # 出口
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
        
        # 拆解
        self.last_node = root
        right = root.right # 要先把 root 的右子樹記下來
        self.flatten(root.left) # 在這個函數內部會把 root 的右邊接成左子樹
        self.flatten(right) # 如果沒先把 root 的右子樹記下來，跑這個函數時會出錯
        
# divide conquer
class Solution:
    def flatten(self, root):
        self.helper(root)
        
    def helper(self, root):
        # 出口
        if root is None:
            return None
        
        # 拆解
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # merge
        # 如果左子樹不是空的，那要把左子樹接到 root 的右邊，把 root 的左邊清空
        # 左子樹的最後一個節點要接上右子樹
        if left is not None:
            left.right = root.right
            root.right = root.left # 要先把左子樹接到 root 的右邊後
            root.left = None # 才把 root 的左邊清空，順序顛倒會出錯
            
        # 如果左右子樹都存在的話，因為前序遍歷的關係 根左右 最後一個節點是右子樹
        # 所以如果右子樹不是空的就要傳回右子樹，這樣再接的時候才不會接錯
        # 如果右子樹是空的，就傳回左子樹
        if right is not None:
            return right
        if left is not None:
            return left
        
        # root 是葉子節點時傳回 root 自己
        return root

# lintcode 453
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    # 改變樹的結構只能用 divide conquer
    # 傳回以 root 為根的子樹平坦過後的結果
    def flatten(self, root):
        # write your code here
        if root is None:
            return None
        
        left_last = self.flatten(root.left) # 傳回子樹的最後一個節點
        right_last = self.flatten(root.right)

        if left_last:
            left_last.right = root.right # 左子樹最後一個點的右邊要接上原本的右子樹
            root.right = root.left
            root.left = None
        
        # 左右子樹都存在的話 flatten 結果最後一個節點會是右子樹的
        if right_last:
            return right_last
            
        if left_last:
            return left_last
        
        return root
