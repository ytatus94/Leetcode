class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles) # 有 n 個 pile

        # dp[i][j] = 從前 i 個 piles 中取出 j 個 coin 所能拿到的最大值
        # 初始條件 dp[0][j] = 0 從前 0 個 pile 無法取出任何的 coin
        dp = [[0] * (k + 1) for i in range(n + 1)]

        # 第 i 個 pile (編號 i - 1) 取 k 個，前 i-1 個 piles 共取 0 個
        # 第 i 個 pile (編號 i - 1) 取 k-1 個，前 i-1 個 piles 共取 1 個
        # 第 i 個 pile (編號 i - 1) 取 k-2 個，前 i-1 個 piles 共取 2 個
        # 第 i 個 pile (編號 i - 1) 取 k-m 個，前 i-1 個 piles 共取 m 個

        for i in range(1, n + 1):
            for j in range(k + 1): # 第 i 個 pile 能取 0 ~ k 個 coins
                # 首先要注意第 i 個 pile (編號 i - 1) 裡面的硬幣數目不可以比能拿的數目 j 多
                total_coins = len(piles[i - 1]) #  有幾個 coins
                allowed_coins = min(j, total_coins) # 最多只能取 j 個 conis
                total_values = 0 # 取 num_coins 後的總價值是多少錢
                for num_coins in range(allowed_coins + 1): # 目前取了幾個 coins
                    if num_coins > 0:
                        total_values += piles[i - 1][num_coins - 1]
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - num_coins] + total_values)
        
        return dp[n][k]
