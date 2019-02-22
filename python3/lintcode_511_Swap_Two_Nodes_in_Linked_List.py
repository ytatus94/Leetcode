"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        node_v1 = None
        node_v2 = None
        
        curr = head
        while curr:
            if curr.val == v1:
                node_v1 = curr
            if curr.val == v2:
                node_v2 = curr
            curr = curr.next
        
        if node_v1 is not None and node_v2 is not None:
            node_v1.val = v2
            node_v2.val = v1
        
        return head
