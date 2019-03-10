# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # traversal 方法一: 改變左右子樹的結構來獲得新的樹
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        self.traverse(root, result) # 先找出 in-order
        
        # 用 in-order 建構新的樹
        for i in range(len(result) - 1):
            result[i].left = None
            result[i].right = result[i + 1]
            
        '''
        用這個方式的時候要注意記得把最後一個節點的左右子樹都設成空，否則會有環
        例如輸入是 [2, 1, null] in-order 是 [1, 2, null] 把 1 的右子樹接到 2 時
        2 本身的左子樹仍然指向 1 就形成了一個環
        '''
        result[-1].left = None
        result[-1].right = None
        
        # 傳回新的樹的根節點
        return result[0]

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        result.append(root)
        self.traverse(root.right, result)

class Solution:
    # traversal 方法二: 用節點的值建立新的樹
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        self.traverse(root, result)
        
        head = TreeNode(result[0])
        curr = head
        for i in range(1, len(result)):
            curr.right = TreeNode(result[i])
            curr = curr.right
        return head
        
    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)

class Solution:
    # divide conquer 方法1:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, tail = self.helper(root)
        return head
        
    # 定義: 傳回以 root 為根的 BST 中最左邊 (最小的) 和最右邊 (最大的) 節點
    def helper(self, root):
        if root is None:
            return None, None
        
        # 拆解
        left_first, left_last = self.helper(root.left)
        right_first, right_last = self.helper(root.right)
        
        # BST 左根右，所以左邊先處理
        if left_last:
            left_last.right = root
            
        root.left = None
        root.right = right_first
        
        # 出口
        # left_first, left_last, right_first, right_last 有可能是空，所以要處理
        first, last = root, root
        if left_first:
            first = left_first
        if right_last:
            last = right_last
        return first, last

class Solution:
    # divide conquer 方法2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.helper(root, None)
    
    # 定義: 傳回以 root 為根的 BST 最左邊 (最小的) 節點
    def helper(self, root, tail):
        if root is None:
            return tail
        
        result = self.helper(root.left, root)
        root.left = None
        root.right = self.helper(root.right, tail)
        return result
