# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        使用快慢指針，快的一次走兩步，慢的一次走一步
        如果有迴圈的話，快的會從後面追上慢的
        '''
        fast, slow = head, head
        while fast and fast.next:
            # 快慢指針
            fast, slow = fast.next.next, slow.next
            
            if fast == slow:
                return True
        return False
        
# lintcode 102
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False
