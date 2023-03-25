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
    @return: The head of linked list.
    """
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return head

        # 要對 Linked list 做更動就需要 dummy
        dummy = ListNode(0, head)
        # 一開始假設第一個節點是排序好的，由第二個節點開始往前面的節點比較
        curr = head.next
        latest_sorted = head # 保存已經排序好的 linked list 的最後一個節點

        while curr is not None:
            if latest_sorted.val <= curr.val:
                latest_sorted = latest_sorted.next # 往下移動
            else:
                prev = dummy # 因為要從頭比較，這樣才能修改第一個節點
                # prev.next 是在 curr 前面，要和 curr 比大小的節點
                # 如果 node 比 curr 小，就往下看下一個
                while prev.next.val <= curr.val:
                    prev = prev.next # 往下移動

                # 跑到這裡的時候 curr 一定比 prev.next 小
                # 所以要把 prev -> prev.next 變成 prev -> curr -> prev.next
                # 還有把 latest_sorted -> curr -> curr.next 變成 latest_sorted -> curr.next
                latest_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = latest_sorted.next
        
        return dummy.next
