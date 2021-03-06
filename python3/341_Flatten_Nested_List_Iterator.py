# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # stack 中是數字的時候 hasNext() 回傳 true
        # 如果下一個是 list 則要想辦法變成數字 
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # 如果 top 是 list，要把 top 的內容變成數字
            # 因為 stack 是後進先出，所以記得順序要反轉
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# lintcode 528
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):
    
    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        self.helper(self.stack, nestedList)

    def helper(self, stack, nestedList):
        
        while nestedList:
            top = nestedList.pop()
            if top.isInteger():
                stack.append(top.getInteger())
            else:
                self.helper(stack, top.getList())
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop(0)
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return len(self.stack) == 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
