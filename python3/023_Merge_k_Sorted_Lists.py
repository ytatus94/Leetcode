# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
        # bottom_up = self.merge_helper_bottom_up(lists, 0, len(lists) - 1)
        # return bottom_up
    
        top_down = self.merge_helper_top_down(lists, 0, len(lists) - 1)
        return top_down

    def merge_helper_bottom_up(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_helper_bottom_up(lists, start, mid)
        right = self.merge_helper_bottom_up(lists, mid + 1, end)
        return self.merge_two_sorted_lists(left, right)

    def merge_two_sorted_lists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next

    def merge_helper_top_down(self, lists, start, end):
        while len(lists) > 1:
            merged_list = []
            start = 0
            end = len(lists) - 1
            while start < end:
                merged_list.append(self.merge_two_sorted_lists(lists[start], lists[start + 1]))
                start += 2
            if (end + 1) % 2 == 1:
                merged_list.append(lists[-1])
            lists = merged_list
        return lists[0]
    
# lintcode 104
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# 用 merge sort 的思路，先切小再由下往上合併 buttom up
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return None
        
        # lists 裡面的元素是 linked list
        return self.merge_helper(lists, 0, len(lists) - 1)

    def merge_helper(self, lists, start, end):
        if start == end:
            return lists[start]
            
        # 把 lists 一直拆分，然後兩兩合併
        mid = start + (end - start) // 2
        left = self.merge_helper(lists, start, mid)
        right = self.merge_helper(lists, mid + 1, end)
        return self.merge_two_lists(left, right)
        
    def merge_two_lists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1 # 移動 tail 到 list1
                list1 = list1.next
            else: # >= 時
                tail.next = list2
                tail = list2 # 移動 tail 到 list2
                list2 = list2.next
            
        # 離開迴圈時，list1 或 list2 其中一個跑完了
        # 要把剩下還沒跑完的接上
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

# 由上往下合併 top down
class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
    
        # 兩兩合併
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists) - 1, 2):
                # 把第 i 個和第 i+1 個 lists 兩兩合併
                merged_list = self.merge(lists[i], lists[i + 1])
                new_lists.append(merged_list)
            
            if len(lists) % 2 == 1:
                # 如果是奇數個，記得要把最後一個元素加入
                new_lists.append(lists[-1])
                
            lists = new_lists
        
        return lists[0]
    
    
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next
