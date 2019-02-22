# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if head is None:
            return head
        if m >= n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # 要反轉第 m 到 n 個的話，需要處理到 m-1 和 n+1 兩個節點
        # 先找出 m-1 和 n 兩個節點
        prev = dummy
        node_m_minus_one = prev
        node_n = prev
        
        for i in range(m-1):
            node_m_minus_one = node_m_minus_one.next
        node_m = node_m_minus_one.next
        
        for j in range(n):
            node_n = node_n.next
        # 把 n+1 節點記錄下來
        node_n_plus_one = node_n.next
        # 然後把 n 的下一個設為空
        node_n.next = None

        prev_curr = None
        curr = node_m
        while curr:
            temp = curr.next
            curr.next = prev_curr
            prev_curr = curr
            curr = temp
            
        node_m.next = node_n_plus_one
        node_m_minus_one.next = node_n
        
        return dummy.next
        
# lintcode 36
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        pre_node_m = self.find_node(dummy, m - 1)
        node_m = pre_node_m.next
        node_n = self.find_node(dummy, n)
        post_node_n = node_n.next

        node_n.next = None
        self.reverse(node_m)
        
        pre_node_m.next = node_n
        node_m.next = post_node_n
        
        return dummy.next
        
    # 把反轉的部分獨立出來
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

    # 找出第 k 個節點
    def find_node(self, head, k):
        node = head
        for i in range(k):
            node = node.next
        return node
