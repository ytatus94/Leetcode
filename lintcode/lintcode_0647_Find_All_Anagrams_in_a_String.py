class Solution:
  def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        result = []


        hash = {}
        for ch in p:
            if ch in hash.keys():
                hash[ch] += 1
            else:
                hash[ch] = 1

        for i in range(len(p)):
            if s[i] in hash.keys():
                hash[s[i]] -= 1

        for i in range(len(s) - len(p) + 1):
            if i > 0:
                if s[i - 1] in hash.keys():
                    hash[s[i - 1]] += 1
                if s[i + len(p) - 1] in hash.keys():
                    hash[s[i + len(p) - 1]] -= 1

            if all(v == 0 for v in hash.values()):
                result.append(i)

        return result
