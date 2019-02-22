# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        '''
        要把 linked list 分成兩組
        一組放比 x 小的，另一組放比 x 大的
        然後再把兩組接起來
        '''
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        
        prev1 = dummy1
        prev2 = dummy2
        
        while head:
            if head.val < x:
                prev1.next = head
                prev1 = head
            else:
                prev2.next = head
                prev2 = head
            head = head.next
            
        # 跑完後 prev1 指向比 x 小的 linked list 的最後一個元素
        # prev2 指向比 x 大的 linked list 的最後一個元素
        # 所以接起來時 prev1 的下一個是第二個 linked list 的第一個元素
        # 還有要注意 prev2 要接上 None
        prev2.next = None
        prev1.next = dummy2.next
        
        return dummy1.next
        
# lintcode 96
"""
Definition of ListNode
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
    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
            
        dummy1 = ListNode(0) # < x
        dummy2 = ListNode(0) # >= x
        
        prev1 = dummy1
        prev2 = dummy2
        curr = head
        
        while curr:
            if curr.val < x:
                prev1.next = curr
                prev1 = curr
            else:
                prev2.next = curr
                prev2 = curr
            curr = curr.next
            
        prev1.next = dummy2.next
        prev2.next = None
        return dummy1.next
