class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        if head.next and head.next.val == head.val:
            # na->(na->na->....->nb->...) 當兩個節點的值相同時
            # 找出下一個不同的節點，並以其為開頭找出正確的 next 讓 na 接上
            while head.next and head.next.val == head.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            # na->(nb->...) 當 val_a != val_b 時，從 nb 開頭的 linked list 中
            # 找出正確的 next 節點，讓 na 接上
            head.next = self.deleteDuplicates(head.next)
            return head

class Solution:      
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 要分成 head.next 是空還不是空兩種
        # 當 head.next 不是空的時候，又要再分成和 head.val 是否相同兩種
        while head:
            # 如果兩個相鄰的節點值不相等，就把 prev 和 head 往下移動
            if head.next and head.next.val != head.val:
                prev = head
                head = head.next
            # 如果兩個相鄰的節點的值相同，就要去找出下一個值不同的節點
            # 然後把 prev.next 指向這個值不同的節點
            elif head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head.next = head.next.next
                # 離開回圈時 head.next 是停在值不同的節點
                prev.next = head.next
                # 先不移動 prev 到 prev.next 因為這個 prev.next 仍有可能和
                # 後面的節點的值相同，所以要繼續找到不同的值的節點才行
                # 移動 prev 的步驟由 if 子句來做
                head = head.next
            elif head.next is None:
                # 如果是空表示現在 head 是最後一個元素了
                # 把 head 移動到 null 後會結束 wile 迴圈
                head = head.next
                
        return dummy.next
    
# lintcode 113
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # 離開迴圈時 head 停在一串相等的值的最後一個
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return dummy.next
