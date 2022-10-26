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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # write your code here
        if head is None:
            return None

        dummy1, dummy2 = ListNode(0), ListNode(0)
        curr1, curr2 = dummy1, dummy2
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = head
            else:
                curr2.next = head
                curr2 = head
            head = head.next

        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next
