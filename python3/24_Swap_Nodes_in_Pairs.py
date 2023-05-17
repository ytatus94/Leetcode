# 方法 1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先用一個假的節點
        root = ListNode(0)
        root.next = head # 假節點的下一個，指向 head
        
        curr = root
        while curr.next and curr.next.next:
            # curr -> p1 -> p2
            p1 = curr.next
            p2 = curr.next.next
            
            # 交換
            curr.next = p2
            p1.next = p2.next
            p2.next = p1
            
            # 交換完後處理下一對
            curr = curr.next.next
        return root.next # 傳回的是 head

# 方法 2.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            n1, n2 = head, head.next
            # 轉換
            if n2:
                temp = n2.next
                n2.next = n1
                n1.next = temp
                prev.next = n2
            # 移動
            prev = head # 就是 n1
            head = head.next

        return dummy.next

# 方法 3.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            n1 = curr.next
            n2 = curr.next.next
            # 交換
            n1.next = n2.next
            n2.next = n1
            curr.next = n2
            # 移動
            curr = curr.next.next
        return dummy.next
