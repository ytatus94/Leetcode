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
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        # 插入：可以插入頭, 插入尾, 插入中間
        # 要被插入的 linked list 可以是空, 只有一個 node, 有很多個 node
        node = ListNode(val)
        if head is None:
            # 頭是空就是空的 linked list
            # 直接傳回 node 就好
            return node

        # 頭不是空的時候，要插入的地方就是插入頭, 插入尾, 或插入中間
        if head.val >= val:
            # 插入頭: 有可能頭比較大也可能和頭相等
            # 這時候都插到頭的前面
            node.next = head
            return node

        curr = head
        while curr is not None:
            if curr.val < val:
                if curr.next is None:
                    # 插入尾
                    curr.next = node
                elif curr.next.val >= val:
                    # 插入中間
                    # 有可能很多個 nodes 和 val 相同
                    # 插入在相同的第一個前面，這樣就不用管相同的有幾個
                    node.next = curr.next
                    curr.next = node
            curr = curr.next

        return head
