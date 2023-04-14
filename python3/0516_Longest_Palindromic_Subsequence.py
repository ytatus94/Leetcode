# 方法 1: 由下往上
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)

        # dp[i][j] = s[i]~s[j] 之間 (就是 s[i:j+1]) 最長的回文串
        dp = [[0 for j in range(n)] for i in range(n)]
        
        for i in range(n - 1, -1, -1): # 這邊 i 要逆著來 loop
            dp[i][i] = 1 # 初始條件，每個字母自己都是回文串
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # 因為 i 逆著來 loop 且 j 順著 loop
                    # 子字串是往頭尾兩邊長
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]) # i 逆著來 loop 的原因是因為要先用到 i+1

        return dp[0][n - 1]

# 方法 2: 由上往下
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # dp[i][j] = s[i] 到 s[j] 的子字串中最長的 palindrome 長度
        dp = [[0 for j in range(n)] for i in range(n)]

        return self.lps(s, 0, n - 1, dp)

    def lps(self, s, start, end, dp):
        # 記憶化搜索
        if dp[start][end] != 0:
            return dp[start][end]
        
        if start > end:
            return 0
        if start == end:
            return 1 # 自己一個字母一定是回文串

        if s[start] == s[end]:
            dp[start][end] = 2 + self.lps(s, start + 1, end - 1, dp)
        else:
            dp[start][end] = max(self.lps(s, start + 1, end, dp), self.lps(s, start, end - 1, dp))

        return dp[start][end]
