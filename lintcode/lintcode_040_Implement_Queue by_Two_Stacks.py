class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = [] # 用來暫時放 stack1 的東西

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        # 只看 stack1 就好
        # 把 stack1 的內容都拿出來放到 stack2
        # 這樣在 stack2 內的順序正好和 stack1 顛倒
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop() # stack2 的最後一個就是 stack1 的第一個
        # 再把全部塞回 stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return res
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack1[0] # 題目說 top 傳回的是第一個元素
