# 方法1: 先把 1->2->3->4->5->null 變成 1->1'->2->2'->3->3'->4->4'->5->5'->null 然後再修改新的節點所指向的 random，最後再拆開成新的 linked list
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
            head.next = new_node.next # head 的下一個點，指回原本的下一個節點，這行必須要寫在 if 條件句前面，否則 new_node.next.next 會指向其他的點
            if new_node.next is not None: # new_node 有可能最後一個點了，所以要檢查 new_node.next 是不是空節點
                new_node.next = new_node.next.next
            head = head.next
        return new_head

    
# 方法2: 用 hash map
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
        hash_map = {}
        curr = head
        while curr:
            new_node = RandomListNode(curr.label)
            new_node.next = curr.next # 先指向原先的 next，等一下再修改
            new_node.random = curr.random # 先指向原先的 random，等一下再修改
            hash_map[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = hash_map[curr]
            if curr.next is not None: # curr 有可能 loop 到 None 了，就不能 .next
                new_node.next = hash_map[curr.next] # 這裡修正 new_node.next 指向的
            if curr.random is not None: # curr 有可能 loop 到 None 了，就不能 .random
                new_node.random = hash_map[curr.random] # 這裡修正 new_node.random 指向的
            curr = curr.next

        return hash_map[head]
