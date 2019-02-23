# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: 'ListNode') -> 'None':
        """
        Do not return anything, modify head in-place instead.
        """
        # 把每個節點塞入 stack 裡面
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        if len(stack) == 0:
            return head
        
        # 把正確的順序放到 reorder 中
        reorder = []
        while len(stack) > 0:
            reorder.append(stack.pop(0))
            if len(stack) > 0:
                reorder.append(stack.pop())
        
        # 做成 linked list
        for i in range(len(reorder) - 1):
            reorder[i].next = reorder[i+1]
        # 記得要把最後一個的下一個指向空    
        reorder[-1].next = None

# lintcode 99
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None:
            return head
        
        mid = self.finde_middle_node(head)
        # tail 是反轉 linked list 後半段之後的起點
        # 也是原本的 linked list 的終點
        tail = self.reverse_linked_list(mid.next)
        
        # 得到前半段與反轉後的後半段兩個 linked list
        mid.next = None
        # 把兩段交叉合併起來
        self.merge(head, tail)
        
    # 用快慢指針找 linked list 的中點，
    # 當離開 while 迴圈的時候 slow 就停在中點上
    def finde_middle_node(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    # 反轉 linked list 
    def reverse_linked_list(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
    def merge(self, head1, head2):
        dummy = ListNode(0)
        while head1 is not None and head2 is not None:
            dummy.next = head1
            dummy = dummy.next
            head1 = head1.next
            
            dummy.next = head2
            dummy = dummy.next
            head2 = head2.next
            
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
