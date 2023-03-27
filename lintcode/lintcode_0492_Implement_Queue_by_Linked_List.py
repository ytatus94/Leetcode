# class ListNode():
#     def __init__(self, val):
#         self.val = val
#         self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        node = ListNode(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        res = self.head.val
        self.head = self.head.next
        return res

    
# 方法 2
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        node = ListNode(item, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node # move tail to node

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.head is None and self.tail is None:
            return -1
        else:
            res = self.head.val
            self.head = self.head.next # move head to the next item
            return res
