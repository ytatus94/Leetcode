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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            # 誰小誰接到 curr 後面
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next # 往下移一格
            else:
                curr.next = l2
                l2 = l2.next # 往下移一格
            curr = curr.next # 往下移一格

        # 如果還有剩下來的部分，就接到 curr 後面
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2

        return dummy.next
