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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        # write your code here
        # 因為題目給 m <= n 所以要考慮相等的情況
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # 找出 m-1, m, n, n+1 四個節點
        # 題目的 m, n 都是從 1 開始算起，所以加一個 dummy node 變成從 0 開始算起
        # 如果 m = 1 的話，那 node_m_minus_one 就剛好是 dummy
        node_m_minus_one = self.find_node(dummy, m - 1)
        node_m = node_m_minus_one.next
        node_n = self.find_node(dummy, n)
        node_n_plus_one = node_n.next

        # 把 node_n 的下一個設為 None 然後就能只反轉 node_m 到 node_n
        node_n.next = None
        self.reverse_linked_list(node_m)

        # 再把反轉後的 linked list 接上原有的部分
        node_m_minus_one.next = node_n
        node_m.next = node_n_plus_one

        # 有可能從 head 就要開始換，所以傳回 dummy.next 比較好
        return dummy.next

    def find_node(self, head, i):
        curr = head
        for j in range(i): 
            curr = curr.next
        return curr

    def reverse_linked_list(self, head):
        if head is None:
            return

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
    
