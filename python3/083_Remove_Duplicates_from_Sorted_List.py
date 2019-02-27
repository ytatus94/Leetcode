# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else: # 當兩個值不相等時，指標才會移往下一個，可避免 [2,2,2] 這種情形
                curr = curr.next
        return head
        
# lintcode 112
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = head
        ptr2 = head.next
        while ptr1:
            while ptr2 is not None and ptr1.val == ptr2.val:
                ptr2 = ptr2.next
            ptr1.next = ptr2
            ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
            
        return dummy.next
