"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None

        # 把兩個 linked list 接起來，形成環狀結構，
        # 然後就可以用 linked list cycle 2 來找出環的入口
        curr = headA
        while curr.next:
            curr = curr.next
        # 離開迴圈時 curr 停在 A 的尾端，curr 是指向最後一個節點

        curr.next = headB

        node = self.linked_cycle_II(headA)
        return node

    def linked_cycle_II(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
