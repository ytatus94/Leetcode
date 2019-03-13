class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res =[]
        for i, v in enumerate(S.split()):
            if v[0] in vowels:
                v += 'ma'
            else:
                v = v[1:] + v[0] + 'ma'
            v += 'a' * (i + 1)
            res.append(v)
        
        return ' '.join(res)
