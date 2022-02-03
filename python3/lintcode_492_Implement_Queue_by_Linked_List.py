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
