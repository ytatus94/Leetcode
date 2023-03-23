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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        dummy = ListNode(0, head)

        cnt1 = 0
        curr1 = head
        while curr1 is not None:
            cnt1 += 1
            curr1 = curr1.next

        cnt2 = 0
        curr2 = dummy
        while curr2 is not None:
            if cnt2 + n == cnt1:
                if curr2.next is not None:
                    curr2.next = curr2.next.next
            cnt2 += 1
            curr2 = curr2.next


        return dummy.next
