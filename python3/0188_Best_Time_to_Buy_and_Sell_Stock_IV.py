class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        n = len(prices)
        
        # 最多可以交易一次，會有三個狀態
        # (沒股票)...(第一次買，持有)...(第一次賣，沒股票)
        # 最多可以交易兩次，會有五個狀態
        # (沒股票)...(第一次買，持有)...(第一次賣，沒股票)...(第二次買，持有)...(第二次賣，沒股票)
        # 最多可以交易三次，會有 7 個狀態
        # 以此類推，最多可以交易 k 次會有 2k + 1 個狀態，奇數是沒股票的狀態，偶數是持有股票的狀態

        dp = [[0 for j in range((2*k + 1) + 1)] for i in range(n + 1)] # 前 i 天位於 j 狀態的最大獲利
        dp[0][1] = 0 # 前 0 天必定是沒股票的狀態，最大獲利=0
        for j in range(2, 2 * k + 2): # j 從 2 開始
            dp[0][j] = float('-inf') # 前零天不可能處於其他狀態

        for i in range(1, n + 1):
            for j in range(1, 2 * k + 2):
                if j % 2 == 1: # 沒有股票的狀態
                    dp[i][j] = dp[i - 1][j]
                    if i >= 2 and j > 1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
                if j % 2 == 0: # 有股票的狀態
                    dp[i][j] = dp[i - 1][j - 1]
                    if i >= 2 and j > 1:
                        dp[i][j] = max(dp[i - 1][j] + prices[i - 1] - prices[i - 2], dp[i][j])

        max_profit = 0
        for j in range(1, 2 * k + 2):
            if j % 2 == 1: # 有賣出才有真正獲利，所以看沒股票的狀態
                max_profit = max(max_profit, dp[n][j])

        return max_profit
