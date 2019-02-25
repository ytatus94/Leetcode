# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        # 1. 先計算 A 和 B 各自的長度，然後可以求得長度差
        # 2. 把比較長的那個，先走長度差步，那剩下來的部分，就和短的那個一樣了
        # 3. 再來就可以兩者同步移動，比較每個節點是否相同
        len_A, len_B = 0, 0
        curr_A, curr_B = headA, headB
        while curr_A:
            len_A += 1
            curr_A = curr_A.next
        while curr_B:
            len_B += 1
            curr_B = curr_B.next
        
        # 2. 不知道 len_A 或 len_B 誰大，所以考慮兩種情形
        curr_A, curr_B = headA, headB # 拉回 head 再走一次
        while len_A > len_B:
            curr_A = curr_A.next
            len_A -= 1
        while len_B > len_A:
            curr_B = curr_B.next
            len_B -= 1
        # 這時候 curr_A 和 curr_B 停留的節點到尾端節點的數目會是一樣的
        
        # 3.
        while curr_A != curr_B:
            curr_A = curr_A.next
            curr_B = curr_B.next
        # 離開迴圈時 curr_A 和 curr_B 會指向同一個節點
        return curr_A
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        set_A = set()
        while headA:
            set_A.add(headA)
            headA = headA.next
        while headB:
            if headB in set_A:
                return headB
            headB = headB.next
        return None

# lintcode 380
