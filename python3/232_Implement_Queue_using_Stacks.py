class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.outStack) == 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.outStack) == 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# lintcode 40
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.in_stack = []
        self.out_stack = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.in_stack.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append( self.in_stack.pop() )
        return self.out_stack.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append( self.in_stack.pop() )
        return self.out_stack[-1]
        
class MyQueue:
    # def __init__(self):
    #     # do intialization if necessary
    #     self.items = []
    # """
    # @param: element: An integer
    # @return: nothing
    # """
    # def push(self, element):
    #     # write your code here
    #     self.items.append(element)
    # """
    # @return: An integer
    # """
    # def pop(self):
    #     # write your code here
    #     if len(self.items) == 0:
    #         return None
    #     return self.items.pop(0)
    # """
    # @return: An integer
    # """
    # def top(self):
    #     # write your code here
    #     if len(self.items) == 0:
    #         return None
    #     return self.items[0]
