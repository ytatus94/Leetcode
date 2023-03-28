# 用 merge sort
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
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sort_list(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None or head.next is None:
            return head

        # 要 O(NlogN) 就用 merge sort
        # 所以首先要做的就是不斷地找出中間點，分成兩段後各自排序
        # 最後在把兩段結果合併起來

        # 找中間點可以用快慢指針
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 當 離開迴圈的時候 slow 會停在中點
        mid = slow.next
        slow.next = None # 要有這一行，能把第一段與第二段分開來

        h1 = self.sort_list(head)
        h2 = self.sort_list(mid)
        return self.merge_all(h1, h2)

    def merge_all(self, h1, h2):
        dummy = ListNode(0)
        curr = dummy

        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next

        if h1 is not None:
            curr.next = h1
        if h2 is not None:
            curr.next = h2

        return dummy.next

# 用 quick sort
