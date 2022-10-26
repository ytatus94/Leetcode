# 方法1: 找出兩個節點後更改值
# lintcode 511
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

# 方法2: 題目說要改點，而不是直接改值
from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
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
    def swap_nodes(self, head: ListNode, v1: int, v2: int) -> ListNode:
        # write your code here
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        prev_n1, prev_n2 = None, None
        while curr:
            if curr.next and curr.next.val == v1:
                prev_n1 = curr
            if curr.next and curr.next.val == v2:
                prev_n2 = curr
            curr = curr.next

        n1, n2 = None, None
        if prev_n1 and prev_n1.next:
            n1 = prev_n1.next

        if prev_n2 and prev_n2.next:
            n2 = prev_n2.next

        if n1 and n2:
            prev_n1.next = n2
            prev_n2.next = n1
            n1.next, n2.next = n2.next,n1.next
        
        return dummy.next

