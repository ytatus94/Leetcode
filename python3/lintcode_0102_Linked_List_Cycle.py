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
        fast = head
        slow = head
        while slow:
            slow = slow.next
            if fast and fast.next: # 要注意 fast 存在才能 fast.next，且 fast.next 存在才能 fast.next.next
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False
      
# 方法2: 與其用 while slow 倒不如直接用 while fast and fast.next 更方便
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
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
