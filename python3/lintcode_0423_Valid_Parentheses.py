class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = [] # save left parentheses
        for ch in s:
            if ch in pairs.keys():
                # if ch is a left parentheses, then put in stack
                stack.append(ch)
            else:
                # if ch is a right parentheses, then the latest item
                # in the stack should be it's corresponding left parentheses
                # otherwise, return false.
                if len(stack) == 0 or pairs[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()
        
        # If all parentheses match, then the stack should be empty
        if len(stack) > 0:
            return False
        else:
            return True
