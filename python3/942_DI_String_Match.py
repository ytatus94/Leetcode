class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        N = len(S)
        A = [i for i in range(N + 1)]
        res = []
        for i in range(N):
            if S[i] == 'I':
                res.append(A.pop(0))
            else:
                res.append(A.pop())
        res.append(A.pop())

        return res
