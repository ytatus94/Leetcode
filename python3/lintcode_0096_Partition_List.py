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
                curr1 = head # curr1 往下移動一格
            else:
                curr2.next = head
                curr2 = head # curr2 往下移動一格
            head = head.next

        curr2.next = None # 要先把 curr2 的最後面接上 None
        curr1.next = dummy2.next # 然後再把 curr1 的後面接上第二個 linked list 的頭
        return dummy1.next # 要傳回第一個 linked list 的頭

