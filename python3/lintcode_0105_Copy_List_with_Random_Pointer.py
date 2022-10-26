"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None

        self.copy_nodes(head)
        self.copy_randoms(head)
        return self.split_list(head)
        
    def copy_nodes(self, head):
        while head is not None:
            new_node = RandomListNode(head.label)
            new_node.next = head.next
            new_node.random = head.random # 必須要有這行
            head.next = new_node
            head = head.next.next

    def copy_randoms(self, head):
        while head is not None:
            new_node = head.next
            if new_node.random is not None: # 因為 27 行的關係，這表示原本的點 head 是有 random 的，既然原本的點 head 有 random，那這個 random 也會複製出新的一個點 head.random.next
                new_node.random = head.random.next # 這邊才把 new_node.random 指向新的 random
            head = head.next.next

    def split_list(self, head):
        new_head = head.next
        while head is not None:
            new_node = head.next
            head.next = new_node.next # head 的下一個點，指回原本的下一個節點
            if new_node.next is not None: # new_node 有可能最後一個點了，所以要檢查 new_node.next 是不是空節點
                new_node.next = new_node.next.next
            head = head.next
        return new_head
