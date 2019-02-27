# lintcode 113
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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # 離開迴圈時 head 停在一串相等的值的最後一個
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return dummy.next
