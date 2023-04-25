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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        if len(stack) == 0:
            return head

        if k > len(stack) and len(stack) > 0:
            k = k % len(stack)

        rotate = stack[len(stack) - k :] + stack[: len(stack) - k]

        for i in range(len(rotate) - 1):
            rotate[i].next = rotate[i + 1]
        rotate[-1].next = None

        return rotate[0]
