class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 開一個長度為 amount + 1 的陣列
        # 其中 dp[i] = 拼出 i 所需要的最少硬幣數目
        dp = [None] * (amount + 1)
        for i in range(amount + 1):
            # 初始條件
            if i == 0:
                dp[0] = 0 # 拼出 0 所需要的最小硬幣數目就是 0
            else:
                # 拼出 i 所需要的最小硬幣數目，這邊先初始化為無限大
                dp[i] = float('inf')

            for j in coins:
                if i >= j and dp[i - j] != float('inf'):
                    dp[i] = min(dp[i], dp[i - j] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
