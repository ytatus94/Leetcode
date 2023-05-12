class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # dp[i][j] = text1 的前 i 個字元和 text2 的前 j 個字元的 LCS
        # 初始條件:
        # dp[i=0][j] = 0: text1 的前 0 個字元時，無法和 text2 組成 LCS
        # dp[i][j=0] = 0: text2 的前 0 個字元時，無法和 text1 組成 LCS
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n][m]
      
 # 用滾動數組
