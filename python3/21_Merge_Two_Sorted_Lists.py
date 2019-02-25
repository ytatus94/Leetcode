# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        root = curr
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # 離開 while 迴圈時，表示其中一個 linked list 已經跑完了 ==> l? = None
        # 這時候只需要接上另一個 linked list 剩下的部分
        curr.next = l1 or l2
        return root.next # 傳回列表的頭

# lintcode 6
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        ptr_a = 0
        ptr_b = 0
        new_list = []
        while ptr_a < len(A) and ptr_b < len(B):
            if A[ptr_a] < B[ptr_b]:
                new_list.append(A[ptr_a])
                ptr_a += 1
            else:
                new_list.append(B[ptr_b])
                ptr_b += 1
        
        while ptr_a < len(A):
            new_list.append(A[ptr_a])
            ptr_a += 1
            
        while ptr_b < len(B):
            new_list.append(B[ptr_b])
            ptr_b += 1
            
        return new_list
