class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        total = 0
        if n == 0:
            return dp[0]
        elif n == 1:
            return dp[1]
        elif n == 2:
            return dp[2]
        else:
            for i in range(3, n + 1):
                total = dp[0] + dp[1] + dp[2]
                dp[0] = dp[1]
                dp[1] = dp[2]
                dp[2] = total
        return total
