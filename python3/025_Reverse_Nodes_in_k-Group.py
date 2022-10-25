# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0) # dummy 的值是隨便取的，主要是要用到 next
        dummy.next = head
        prev = dummy
        while prev:
            prev = self.reverseKNodes(prev, k)
        return dummy.next
        
        
    def reverseKNodes(self, prev, k):
        '''
        這裡專門只看 k 個點時
        基本上就是普通的 reverse linked list 只是一次只反轉 k 個
        prev -> (n1 -> n2 -> n3 -> ... -> nk) -> nk+1
        會變成 prev -> (nk -> nk-1 -> ... -> n1) -> nk+1
        原本的 head 會是 n1，但是整個 reverse 的過程還會影響到 prev 和 nk+1
        所以還要考慮到 prev 和 nk+1
        回傳時，要回傳下一個組的 head 的前一個，也就是這個組反轉後的最後一個 (就是 n1)
        '''
        node_k = prev
        # 先檢查每一個節點 node_k 存不存在，要存在才能 .next
        for i in range(k):
            if node_k is None:
                return
            node_k = node_k.next # node_k 要存在才能 .next
            
        if node_k is None: # 走完 for 迴圈後，指標會停在 nk，且 nk 一定要存在
            return
        
        # nk 要存在才能 .next
        node_k_plus_one = node_k.next # 要先記住 nk+1
        
        # 這邊才開始做反轉的動作
        # 要把指標拉回 linked list 一開始的地方，再用 for 迴圈跑一次
        prev_curr = prev
        curr = prev.next
        for i in range(k): # 這邊就是很普通的 reverse linked list
            temp = curr.next
            curr.next = prev_curr
            prev_curr = curr
            curr = temp
            
        # 反轉完了，現在要把 prev 和 nk+1 接到反轉後的 linked list 上
        # 原本的 n1 其實就是 prev.next，這時候要把 n1 --> nk+1，這個要先做
        node1 = prev.next
        # 然後才把 prev.next 改成 nk
        node1.next = node_k_plus_one
        prev.next = node_k
        
        return node1

# lintcode 450
"""
Definition of ListNode
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
    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        while prev:
            prev = self.reverse_k_node(prev, k)
        
        return dummy.next
    
    # 傳回反轉前的第一個點 (就是反轉後的最後一個點)
    # 不夠 k 個點就回傳 None 不反轉
    def reverse_k_node(self, prev, k):
        if k <= 0:
            return None
        
        if prev is None:
            return None
        
        nodek = prev
        node1 = prev.next
        
        for i in range(k):
            if nodek is None:
                return None
            nodek = nodek.next
              
        if nodek is None:
            return None
        
        nodekplus = nodek.next
        
        prev_curr = prev
        curr = prev.next
        
        for i in range(k):
            temp = curr.next
            curr.next = prev_curr
            prev_curr = curr
            curr = temp
            
        node1.next = nodekplus
        prev.next = nodek
        
        return node1
