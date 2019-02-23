"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    # 樹的結構發生變化時只能用 divide conquer
    # 傳回以 root 為根，刪掉 value 節點的子樹
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return None
            
        # 如果有找到就要把那個節點刪掉
        if root.val == value:
            # 左右子樹都是空，就只是刪掉 root
            # 如果右子樹是空，但是左子樹不是空，就把左子樹的最大值搬到 root 的位置
            # 如果右子樹不是空，就把右子樹的最小值搬到 root 的位置
            if root.left is None and root.right is None:
                root = None
            elif root.right is None:
                max_node = self.find_bst_max(root.left)
                root.val = max_node.val
                root.left = self.removeNode(root.left, max_node.val)
            else:
                # 把右子樹的最小值搬過來
                # 然後再去右子樹裡面刪掉那個最小值
                min_node = self.find_bst_min(root.right)
                root.val = min_node.val
                root.right = self.removeNode(root.right, min_node.val)
            
            return root
            
        # 如果要找的值比 root 的值還小，那就會在 root 的左子樹裡面
        # 如果要找的值比 root 的值還大，那就會在 root 的右子樹裡面
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        
        # 最後還是要傳回 root
        return root
        
    def find_bst_min(self, root):
        if root is None:
            return None
        
        # root 的左子樹一定比 root 小，右子樹一定比 root 大
        # 所以左子樹是空的時候，root 一定是最小值
        if root.left is None:
            return root
        else:
            return self.find_bst_min(root.left)
            
    def find_bst_max(self, root):
        if root is None:
            return None
        
        # root 的右子樹一定比 root 大
        # 要是右子樹是空，root 一定是最大值
        if root.right is None:
            return root
        else:
            return self.find_bst_max(root.right)
