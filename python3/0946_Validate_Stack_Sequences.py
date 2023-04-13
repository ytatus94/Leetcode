class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed is None or len(pushed) == 0:
            return False
        if popped is None or len(popped) == 0:
            return False
        if len(pushed) != len(popped):
            return False

        stack = []
        for i in pushed:
            stack.append(i)
            while len(popped) > 0 and len(stack) > 0 and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
        
        while len(popped) > 0:
            if popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
            else:
                return False

        return len(stack) == 0

# 方法 2:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        
        for i in pushed:
            stack.append(i)
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
