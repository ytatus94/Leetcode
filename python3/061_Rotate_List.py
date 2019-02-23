# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if head is None:
            return head
        
        # 計算 linked list 的長度
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        # offset 可能會比 linked list 的長度還要長
        # 所以要重新計算
        k = k % size
        
        if k == 0:
            return head
        
        # 要找出新的起點
        # n1, n2, n3, n4, n5, k=3
        # 從 head (n1) 出發，走完後會停在 n3
        # 所以 n4 是新的起點，然後 n3.next 要指向 None
        node = head
        # 因為從 head 出發所以只移動 size -k -1
        # 如果是從 dummy 出發就移動 size -k
        for i in range(size - k - 1):
            node = node.next
        new_head = node.next # 循環後新的起點
        node.next = None # node 變成循環後的終點，所以下一個指向 None
        
        # 從新的起點出發走到原本 linked list 中的最後一個元素 (tail)
        # 然後再把最後一個元素接上 head
        # 從 n4 出發找到 n5，然後把 n5 接上 n1
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        return new_head
