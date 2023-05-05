# 方法 1.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split(' ')

        if len(pattern) != len(new_s):
            return False
        
        # set(string) 會把 string 拆成字母
        if len(set(pattern)) != len(set(new_s)):
            return False

        n = len(pattern)
        hash = {}
        for i in range(n):
            if pattern[i] in hash.keys():
                hash[pattern[i]].add(new_s[i])
            else:
                # 如果用 set(new_s[i]) 會被拆開成每個字母
                hash[pattern[i]] = set()
                hash[pattern[i]].add(new_s[i])

        for k, v in hash.items():
            if len(v) > 1:
                return False

        return True

# 方法 2.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        if len(pattern) != len(s):
           return False 
        if len(set(pattern)) != len(set(s)):
            return False

        hash = {}
        for i in range(len(pattern)):
            if pattern[i] in hash.keys():
                if hash[pattern[i]] != s[i]:
                    return False
            else:
                # 如果有相同的 pattern[i] 但是不同的 s[i]
                # hash[pattern[i]] 會被新的 s[i] 覆寫
                hash[pattern[i]] = s[i]

        return True
