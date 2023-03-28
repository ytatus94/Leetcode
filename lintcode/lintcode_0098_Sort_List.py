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
        if head is None or head.next is None: # 沒有節點，或只有一個節點
            return head

        # 要 O(NlogN) 所以用 quick sort
        # 先選出 pivot 然後比 pivot 小的放左邊，比 pivot 大的放右邊
        
        # 用快慢指針找中點，然後把中點當 pivot
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # while loop 出來的時候, slow 停在 中點
        mid = slow

        # 分段，因為是 linked list 所以要分成左中右三段
        # 用中點當作 pivot，但是因為是 Linked list 所以中點是自己一段
        # 有可能有好幾個節點的數值與 pivot 一樣，所以 mid 可能不只一個節點
        left_dummy, right_dummy, mid_dummy = ListNode(0), ListNode(0), ListNode(0)
        left_tail, right_tail, mid_tail = left_dummy, right_dummy, mid_dummy

        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = left_tail.next
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = right_tail.next
            else:
                mid_tail.next = head
                mid_tail = mid_tail.next
            head = head.next

        # 把尾巴接上 None
        left_tail.next = None
        right_tail.next = None
        mid_tail.next = None

        # 左右各自排序
        left = self.sort_list(left_dummy.next)
        right = self.sort_list(right_dummy.next)
        
        # 數列的 quick sort 不需要合併，因為是直接交換指向的數值，數列本身仍是完整的
        # linked list 的 quick sort 因為先前拆開成三段了，要先合併成一個完整的 linked list 才行
        dummy = ListNode(0)
        tail = dummy
        while left:
            tail.next = left
            left = left.next
            tail = tail.next
        # 結束時，tail 停在 left 的最後一個上
        mid_curr = mid_dummy.next # 注意要從 mid 的頭開始接
        while mid_curr:
            tail.next = mid_curr
            mid_curr = mid_curr.next
            tail = tail.next
        # 結束時，tail 停在 mid 上
        while right:
            tail.next = right
            right = right.next
            tail = tail.next
        # 結束時，tail 停在 right 的最後一個上
        return dummy.next # 傳回合併後，完整的 linked list

