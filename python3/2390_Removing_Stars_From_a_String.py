class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i != '*':
                res.append(i)
            else:
                if len(res) > 0:
                    res.pop()
                else:
                    continue
        res = ''.join(res)

        return res
