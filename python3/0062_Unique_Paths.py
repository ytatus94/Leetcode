# lintcode 114
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 1 or n == 1:
            return 1
            
        rows = m
        cols = n
        # status
        f = [[None for col in range(cols)] for row in range(rows)]
        
        # initialize
        # 第一行和第一列都初始化為 1
        for row in range(rows):
            f[row][0] = 1
        for col in range(cols):
            f[0][col] = 1
            
        # function: top-down
        for row in range(1, rows):
            for col in range(1, cols):
                f[row][col] = f[row - 1][col] + f[row][col - 1]
                
        return f[rows - 1][cols - 1]

# 方法 2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 開一個二維陣列紀錄走到 (i, j) 有幾種方式
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # 初始條件: 一開始在原點只有一種方式
                    dp[i][j] = 1
                elif i == 0:
                    # 最上面的 row 只可能從左邊的格子走過來
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    # 最左邊的 column 只可能從上面的格子走過來
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
