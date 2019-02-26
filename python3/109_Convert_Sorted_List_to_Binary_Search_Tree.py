# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # BST 是用中序遍歷 (左根右)
        # 所以 root 會是 linked list 正中間的那個節點
        # 要先找到 root 的節點，左半邊的 linked list 用來構成左子樹
        # 右半邊的 linked list 用來構成右子樹
        
        # 出口:
        if head is None:
            return None
        
        # 找 root
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        # 離開回圈時 slow 會停在正中間的節點上
        # prev 停在 slow 前一個節點上，要把 prev 接上 None
        # 才能形成用來構成左子樹的 linked list
        if prev is not None:
            prev.next = None
        mid = slow
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    
# lintcode 106
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        # BST 是用中序遍歷 (左根右) 所以 linked list 的中點就是 root
        if head is None:
            return None
            
        mid = self.find_middle(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
        
    def find_middle(self, head):
        prev = None
        fast, slow = head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        # 離開時 slow 是停在中間
        # (n1->n2->...->prev)->slow->(nk->nk+1->...->ntail)->null
        # 要把 prev 接上 None 才能形成兩段 (用來構成左子樹的)->root->(用來構成右子樹的)->null
        if prev:
            prev.next = None
        return slow
