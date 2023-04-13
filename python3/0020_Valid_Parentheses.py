class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        mapping = {')': '(', ']': '[', '}': '{'}

        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else: # i = ')', ']', '}'
                if len(stack) > 0 and mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
