"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """
    def toArrayList(self, head):
        # write your code here
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res
