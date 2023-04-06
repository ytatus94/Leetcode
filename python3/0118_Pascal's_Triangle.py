class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return 0

        dp = [[0 for j in range(i)] for i in range(1, numRows + 1)]

        for i in range(1, numRows + 1):
            for j in range(i):
                # 初始化 dp[0][0] = 1, dp[i][0] = 1 dp[i][i] = 1
                if j == 0 or j == i - 1:
                    dp[i - 1][j] = 1
                elif i > 2:
                    dp[i - 1][j] = dp[i - 2][j - 1] + dp[i - 2][j]

        return dp
