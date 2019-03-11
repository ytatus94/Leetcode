class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        uncommon = {}
        for word in A.split():
            if word in uncommon:
                uncommon[word] += 1
            else:
                uncommon[word] = 1
        for word in B.split():
            if word in uncommon:
                uncommon[word] += 1
            else:
                uncommon[word] = 1
        res = []
        for k, v in uncommon.items():
            if v == 1:
                res.append(k)
        return res
