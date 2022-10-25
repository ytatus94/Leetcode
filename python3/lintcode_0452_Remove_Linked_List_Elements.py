"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        # 因為要被刪除的可能包含 head 所以要建立一個新的 linked list 用來保存結果
        dummy = ListNode(0) # dummy.next 才是要傳回的，但是 dummy.next 是什麼現在還不知道
        curr = dummy
        while head is not None:
            while head is not None and head.val == val:
                head = head.next
            curr.next = head
            curr = curr.next
            if head is not None:
                head = head.next
        return dummy.next
