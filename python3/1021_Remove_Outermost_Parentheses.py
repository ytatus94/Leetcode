class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        queue = list()
        count = 0
        primitive = None
        for i in S:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            
            if count == 0:
                queue.append(primitive[1:])
                primitive = None
            else:
                if primitive is None:
                    primitive = i
                else:
                    primitive += i
              
        return "".join(queue)
