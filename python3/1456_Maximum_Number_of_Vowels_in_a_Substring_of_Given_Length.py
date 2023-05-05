# 方法 1.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0

        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_counts = 0
        for i in range(k):
            if s[i] in vowels:
                print(i, s[i])
                vowel_counts += 1
        
        result = vowel_counts

        i, j = 0, k - 1
        while i < len(s) - k:
            j += 1
            if s[j] in vowels:
                vowel_counts += 1
            if s[i] in vowels:
                vowel_counts -= 1
            i += 1

            result = max(result, vowel_counts)

        return result

# 方法 2.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        count = 0
        # 先看前 k 個有多少母音
        for i in range(k):
            if s[i] in 'aeiou':
                count += 1
        
        result = count

        # 再從第 k+1 個看到最後一個
        # 如果 sliding window 尾巴新增的那個字母是母音就加一
        # 如果 sliding window 頭去掉的字母是母音就減一
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                count += 1
            if s[i - k] in 'aeiou':
                count -= 1

            result = max(result, count)

        return result
