# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 用 merge sort
        if head is None or head.next is None:
            return head
        # 1. 切兩半
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        # 2. 兩半各自 merge sort
        # 傳回的是排序後的第一個節點
        h1 = self.sortList(head)
        h2 = self.sortList(mid)
        # 3. 合併排序後的兩半，然後傳回第一個節點
        return self.merge(h1, h2)
    
    def merge(self, h1, h2):
        dummy = ListNode(0)
        curr = dummy
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        # 如果某一段跑完了，另一段卻還有剩，就把剩下的接上
        if h1 is None:
            curr.next = h2
        if h2 is None:
            curr.next = h1
            
        return dummy.next
        
# lintcode 98
