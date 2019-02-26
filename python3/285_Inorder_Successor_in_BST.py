# lintcode 448
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    # 純 traversal
    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None:
            return None
        
        self.pre = None
        self.succ = None
        
        self.helper(root, p)
        return self.succ
        
    def helper(self, root, p):
        if root is None:
            return
        
        self.helper(root.left, p)
        
        if self.pre == p:
            self.succ = root
        self.pre = root
        
        self.helper(root.right, p)

class Solution:
    # 傳回以 root 為根中，p 的下一個節點
    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None:
            return None
        
        # 因為是 BST 有著 in-order 大小的順序
        # p 的右子樹不是空的話，那 successor 一定是在右子樹裡面的最小值
        if p.right:
            return self.find_min(p.right)
            
        # 如果 p 的右子樹是空，那就從 root 開始往下找
        # 如果 p.val > root.val 就往 root 的右子樹找
        # 如果 p.val < root.val 就往 root 的左子樹找
        succ = None
        while root:
            if p.val < root.val:
                # 如果 p 在 root 的左子樹，有可能 root.left = p
                # 所以要先把 root 記成 succ
                succ = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                break
        
        return succ
        
    def find_min(self, root):
        if root.left:
            root = root.left
        return root

class Solution:
    # 笨方法：先找出中序遍歷，然後從中序遍歷中找 p 的下一個點
    def inorderSuccessor(self, root, p):
        if root is None:
            return None
            
        res = self.inorderTraversal(root)
        p_index = res.index(p)
        
        if p_index < len(res) - 1:
            successor = res[p_index + 1]
            return successor
            
        return None

    def inorderTraversal(self, root):
        results = []
        if root is None:
            return results
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        results += left
        results.append(root) # 提交之後 lintcode 要吃的是 node 不是 node.val
        results += right
        
        return results
