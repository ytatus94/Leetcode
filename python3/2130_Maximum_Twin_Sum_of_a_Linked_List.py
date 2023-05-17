# 方法 1. 直接看節點的數值
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_values = []
        while head:
            node_values.append(head.val)
            head = head.next

        left, right = 0, len(node_values) - 1
        result = 0
        while left < right:
            result = max(result, node_values[left] + node_values[right])
            left += 1
            right -= 1

        return result

# 方法 2. 用快慢指針，找中點，反轉其中一個 linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 用快慢指針找中點
        # 找到後可以把前半段或是後半段 linked list 反轉
        # 如果反轉後半段的話，還要多一個 while 迴圈
        # 如果反轉前半段的話，可以一邊找中點一邊反轉，比較快
        fast, slow = head, head
        prev = None
        while fast:
            fast = fast.next.next
            # slow 一邊前進一邊反轉
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # 當離開回圈的時候 fast = Null, slow=後半段的頭,
        # prev = 原先前半段的尾，但因為反轉前半段了，所以是反轉後的頭
        
        result = 0
        while prev:
            result = max(result, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return result
