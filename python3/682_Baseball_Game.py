class Solution:
    def calPoints(self, ops: List[str]) -> int:
        valid = []
        for i in ops:
            if i == 'C':
                valid.pop()
            elif i == 'D':
                valid.append(valid[-1] * 2)
            elif i == '+':
                valid.append(valid[-1] + valid[-2])
            else:
                valid.append(int(i))
        
        return sum(valid)
