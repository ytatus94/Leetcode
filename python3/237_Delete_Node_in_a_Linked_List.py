# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''沒有要回傳任何東西，單純刪掉 node'''
        node.val = node.next.val
        node.next = node.next.next
        
# lintcode 372
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
