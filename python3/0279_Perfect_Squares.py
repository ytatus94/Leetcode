class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1): # j 跑到 sqrt(i) 就好
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

# O(N^2) 超時了
class Solution:
    def numSquares(self, n: int) -> int:
        # 如果 n 本身是完全平方數，那最少的完全平方數之和就是 1
        sqrt_n = int(n**0.5)
        if sqrt_n * sqrt_n == n:
            return 1

        # i 最少能被分成幾個完全平方數之和
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0

        for i in range(n + 1):
            for j in range(i + 1): # j 可以等於 i
                # 如果 j 的平方比 i 小(或相等) 那 j 就是組成 i 的其中一個完全平方數
                if i >= j * j:
                    dp[i] = min(dp[i], dp[i - j * j] + 1) # +1 表示 j 這一個數

        return dp[n]
