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
"""
Definition of ListNode
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
    def sortList(self, head):
        # write your code here
        if head is None:
            return head
        
        # result = self.merge_sort(head)
        result = self.quick_sort(head)
        return result
        
    # 定義：拆成兩半，每個半段各自做 merge sort，然後再合併
    def merge_sort(self, head):
        # 出口：只剩下 head 一個元素
        if head.next is None:
            return head
        
        # 找中點
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 離開回圈時 slow 是指向 linked list 中間節點
        # linked list 可以藉由 slow 分成兩段
        # 所以第一個節點到 slow 是第一段，slow.next 到最後一個節點是第二段
        head2 = slow.next # 後半段的頭節點
        slow.next = None # 要記得把前半段的尾巴接上 None 才能形成兩前後兩段 linked list
        
        # 拆解：
        list1_head = self.merge_sort(head)
        list2_head = self.merge_sort(head2)
        return self.merge(list1_head, list2_head)
        
    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        
        # 把節點合併起來
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # 當其中一個已經跑完了，就把另一個剩下的全部接上
        if list1 is None:
            curr.next = list2
        elif list2 is None:
            curr.next = list1
            
        return dummy.next
        
    # 定義：每個節點和 pivot 比較大小，可以分成三種:
    # 1. 比 pivot 小的 linked list
    # 2. pivot 自己
    # 3. 比 pivot 大的 linked list
    # 每一段各自做 quick sort 後再合併起來
    def quick_sort(self, head):
        # 出口:
        if head is None or head.next is None:
            return head
        
        mid = self.find_middle(head)
        
        left_dummy, right_dummy, mid_dummy = ListNode(0), ListNode(0), ListNode(0)
        left_tail, right_tail, mid_tail = left_dummy, right_dummy, mid_dummy
        # 把 linked list 分成三段: 比 mid 小的，比 mid 大的，等於 mid 的
        while head is not None:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = head
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = head
            else:
                mid_tail.next = head
                mid_tail = head
            head = head.next
            
        # 把每一段的結尾接上 None
        left_tail.next, right_tail.next, mid_tail.next = None, None, None
        
        # 各自排序每一段
        left = self.sortList(left_dummy.next)
        right = self.sortList(right_dummy.next)
        
        # 合併
        return self.concat(left, mid_dummy.next, right)
        
    def find_middle(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
    def concat(self, left, middle, right):
        dummy = ListNode(0)
        tail = dummy
        tail.next = left
        while tail.next:
            tail = tail.next
            
        tail.next = middle
        while tail.next:
            tail = tail.next
            
        tail.next = right
        while tail.next:
            tail = tail.next
            
        return dummy.next
