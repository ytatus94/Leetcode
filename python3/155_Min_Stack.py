class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: 'int') -> 'None':
        self.items.append(x)

    def pop(self) -> 'None':
        if len(self.items) != 0:
            self.items.pop() # 只要移除 stack 中最後一個，但不需要回傳

    def top(self) -> 'int':
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def getMin(self) -> 'int':
        if len(self.items) == 0:
            return None
        return min(self.items)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# lintcode 12
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.items = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.items.append(number)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.items) == 0:
            return None
        return self.items.pop()
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if len(self.items) == 0:
            return None
        return min(self.items)
