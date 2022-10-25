# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        
        '''
        需要兩個指標 curr 和 prev 分別保存現在的節點和上一個節點
        要反轉，所以目標是要把 curr.next = prev
        但是這麼一來原先的 curr.next 所指向的東西的資訊就不見了
        因此就需要另一個變數 temp 先保存原先的 curr.next
        '''
        prev = None
        curr = head
        
        while curr:
            temp = curr.next # 先保存原先所指向的東西
            curr.next = prev # 反轉
            prev = curr # prev 和 curr 往下移動一個節點
            curr = temp
        
        # 離開 while 迴圈後:
        # curr 是原先 linked list 的最後一個節點的下一個 (就是空)
        # 而此時 prev 是原先 linked list 的最後一個節點
        # 所以 prev 正好是反轉後的第一個節點，所以回傳 prev
        return prev

# lintcode 35
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
