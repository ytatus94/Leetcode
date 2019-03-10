# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        這題用快慢指針，快的一次走兩步，慢的一次走一步
        當快地走到底的時候，慢的會走到中間 (基數個元素的時候)
        當快的走到底的前一個時，慢的走到兩個中間值的第一個 (偶數個元素時)
        '''
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 離開迴圈時 fast 會是最後一個 (基數個元素) 或是最後一個的前一個 (偶數個元素)
        if fast.next == None: # 基數個元素時
            return slow
        else: # 偶數個元素時
            return slow.next
