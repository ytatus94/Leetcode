# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # 用快慢指針先找出第 k 個節點
        fast = dummy
        for i in range(k):
            fast = fast.next

        node1 = fast # 從頭算起的第 k 個節點

        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        # 當離開迴圈時 fast 是 None, slow 停在從尾端算起的第 k 個節點上

        node1.val, slow.val = slow.val, node1.val

        return dummy.next
