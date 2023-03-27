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

# 方法 2 用快慢指針
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
        # 當快慢指針差 n 個 node
        # 當 fast 走到結尾的 Null 時，slow 會停在要刪除的 node 上面
        fast = head
        for _ in range(n):
            fast = fast.next
        # 希望 fast 走到 Null 時, slow 停在要刪除的 node 的前一個
        # 所以 slow 就從 dummy 開始
        slow = dummy
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
