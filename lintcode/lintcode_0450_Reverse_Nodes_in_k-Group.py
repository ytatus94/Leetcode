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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        # 要改變 linked list 的結構的時候，就需要用到 dummy node
        dummy = ListNode(0)
        dummy.next = head

        # dummy 不可以動，但是又需要處理到 head 前面一個，所以需要 prev
        prev = dummy

        while prev:
            prev = self.reverse_K_node(prev, k)

        return dummy.next

    def reverse_K_node(self, prev, k):
        # 先檢查 prev 後面是否有 k 個節點可以反轉，如果沒有 k 個節點，就不反轉
        is_reversible = self.check_number_of_nodes(prev, k)
        if not is_reversible:
            return None # 這邊要 return None 這樣 while prev: 才會停止

        # 因為只反轉 k 個點，所以有四個重要的點要處理 prev, n1, nk, nk+1
        # prev 是傳入的參數
        n1 = prev.next
        nk = self.find_node(prev, k) # prev 必須是第一個的前一個
        nk_plus_one = nk.next

        # 把 nk 的下一個設成 None 後就可以開始反轉了
        nk.next = None
        self.reverse_linked_list(n1)

        # 反轉完 nk 會是第一個點，n1 會是最後一個點
        # 再把前後的 prev 和 nk+1 接上
        prev.next = nk
        n1.next = nk_plus_one

        return n1

    def check_number_of_nodes(self, prev, k):
        if k <= 0:
            return False

        curr = prev
        for i in range(k):
            if curr is None:
                return False
            curr = curr.next

        # 離開迴圈時 curr 是停在最後一個點，但是最後一個點有可能是 None
        # 所以要判斷一下
        if curr is None:
            return False
        
        return True

    def find_node(self, head, k):
        curr = head
        for i in range(k):
            curr = curr.next
        return curr

    def reverse_linked_list(self, head):
        if head is None:
            return None

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
