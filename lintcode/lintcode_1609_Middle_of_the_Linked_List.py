"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        curr_1 = head
        curr_2 = head
        while curr_1.next is not None:
            print(curr_1.val, curr_2.val)
            if curr_1.next.next is not None:
                curr_1 = curr_1.next.next
                curr_2 = curr_2.next
            else:
                curr_1 = curr_1.next # 這樣一來 curr_1 一定會移動到最後一個 node 然後結束 while loop 
                curr_2 = curr_2.next
        return curr_2
