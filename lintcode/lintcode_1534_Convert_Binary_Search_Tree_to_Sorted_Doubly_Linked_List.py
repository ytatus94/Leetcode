"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        if root is None:
            return None

        self.first_node = None
        self.last_node = None
        # 因為是 BST 用中序遍歷 (左根右) 得到 node 的順序
        self.inorder(root)

        # 題目要求環狀，所以要把第一個和最後一個節點連接起來
        # 左子樹 --> 上一個點
        # 右子樹 --> 下一個點
        self.first_node.left = self.last_node
        self.last_node.right = self.first_node

        return self.first_node

    def inorder(self, root):
        if root is None:
            return

        # 先看左邊
        # 因為是 BST 一直先進左子樹，就可以找到最小的節點
        self.inorder(root.left)

        # 再看根
        # 找到最小的節點後就設成 first
        if self.first_node is None:
            self.first_node = root
        
        # 找目前為止最大的節點
        if self.last_node is None:
            self.last_node = root # 這個情形只發生在 node 剛好是最小節點的時候
        else:
            self.last_node.right = root # 把上一個遞歸中的最大節點的右邊接上當前 node
            root.left = self.last_node # 把當前 node 的左邊接到上一個遞歸中的最大節點
            self.last_node = root # 在把最大節點改成當前 node

        # 最後看右邊
        self.inorder(root.right)
