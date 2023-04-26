# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        temp = 0 # 用來記錄上一個節點倆倆相加後超出個位數的部分

        while l1 and l2:
            total = l1.val + l2.val + temp
            temp = total // 10

            node = ListNode(total % 10) # 只取個位數
            
            curr.next = node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        # 如果 l1 還有剩
        while l1:
            total = l1.val + temp
            temp = total // 10

            node = ListNode(total % 10)

            curr.next = node
            curr = curr.next
            
            l1 = l1.next

        # 如果 l2 還有剩
        while l2:
            total = l2.val + temp
            temp = total // 10

            node = ListNode(total % 10)

            curr.next = node
            curr = curr.next
            
            l2 = l2.next

        # 可能 l1, l2 都沒剩了，但是 temp 還有剩
        if temp > 0:
            node = ListNode(temp)
            curr.next = node
            curr = curr.next

        return dummy.next

# 方法 2: 把上面的三個 while 和一個 if 合併起來
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        temp = 0 # 用來記錄上一個節點倆倆相加後超出個位數的部分

        while l1 is not None or l2 is not None or temp != 0:
            l1_val, l2_val = 0, 0

            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next

            total = l1_val + l2_val + temp
            temp = total // 10

            node = ListNode(total % 10) # 只取個位數
            
            curr.next = node
            curr = curr.next

        return dummy.next
