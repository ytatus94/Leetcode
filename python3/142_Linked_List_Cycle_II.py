# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先用快慢指針找出相遇點
        fast, slow = head, head
        while True:
            # 先判斷是否有 cycle
            if fast == None or fast.next == None:
                return None
            
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break # 相遇時就中斷，此時指標會指在相遇點上
                
        # 用兩個等速指標，一個從頭走，一個從相遇點走
        # 當兩者相遇的時候，就是 cycle 的起點
        meet = fast
        while meet != head:
            head = head.next
            meet = meet.next
        return meet
        
# lintcode 103
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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
            
        while head and slow:
            if head == slow:
                return head
            head = head.next
            slow = slow.next
