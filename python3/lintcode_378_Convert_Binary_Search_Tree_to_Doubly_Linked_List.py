"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class ResultType:
    first, last = None, None
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    # 結構發生變化了，只能用 divide conquer
    def bstToDoublyList(self, root):
        # write your code here
        if root is None:
            return None
            
        result = self.helper(root)
        return result.first
        
    def helper(self, root):
        if root is None:
            return None
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        node = DoublyListNode(root.val)
        
        result = ResultType(None, None)
        
        # 題目說要用 in-order: 左根右
        if left is None:
            result.first = node
        else:
            result.first = left.first
            left.last.next = node
            node.prev = left.last
            
        if right is None:
            result.last = node
        else:
            result.last = right.last
            right.first.prev = node
            node.next = right.first
            
        return result
