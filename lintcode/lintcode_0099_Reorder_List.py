from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorder_list(self, head: ListNode):
        # write your code here
        if head is None:
            return head

        mid = self.find_middle_node(head)
        tail = self.reverse_linked_list(mid.next)

        mid.next = None
        self.merge(head, tail)

    def find_middle_node(self, head):
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_linked_list(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def merge(self, head1, head2):
        dummy = ListNode(0)
        while head1 is not None and head2 is not None:
            dummy.next = head1
            dummy = dummy.next
            head1 = head1.next

            dummy.next = head2
            dummy = dummy.next
            head2 = head2.next

        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
