# 方法 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        # 最多只能交易兩次，所以可以分成五個階段
        # (a 沒股票)...(b 第一次買入並持有)....(c 第一次賣出後無股票)...(d 第二次買入並持有)...(e 第二次賣出後沒股票)
        # 要探討在第 i 天時，位於哪個階段 j
        dp = [[0 for j in range(5 + 1)] for i in range(len(prices) + 1)] # 前 i 天位於某階段 j 的最大獲利

        dp[0][1] = 0 # 前 0 天一定處於 (a 沒股票) 的狀態，最大獲利 = 0
        for j in range(2, 6):
            dp[0][j] = float('-inf') # 前 0 天不可能處於 (b, c, d, e) 的狀態，所以獲利是 -inf

        for i in range(1, len(prices) + 1):
            # 1.) 前 i 天 (第 i-1 天) 結束時，手上沒股票 (可能是 a, c, e 的階段)
            # 可能是前 i-1 天 (第 i-2 天) 也沒股票
            # 可能是前 i-1 天 (第 i-2 天) 有股票，第 i-1 天賣掉並獲利
            for j in [1, 3, 5]:
                dp[i][j] = dp[i - 1][j]
                if i >= 2 and j > 1: # 注意 j 不能等於 1 因為會 j-1=0 沒有這個階段
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
            # 2.) 前 i 天 (第 i-1 天) 結束時，手上有股票 (可能是 b, d 的階段)
            # 可能是前 i-1 天 (第 i-2 天) 手上有股票
            # 可能是前 i-1 天 (第 i-2 天) 手上沒股票，但是第 i-1 天買入
            for j in [2, 4]:
                dp[i][j] = dp[i - 1][j - 1]
                if i >= 2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])

        return max(dp[len(prices)][1], dp[len(prices)][3], dp[len(prices)][5])

# 方法 2:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        # 最多發生兩次交易，發生兩次交易一定比發生一次交易還賺錢
        cost1, cost2 = float('inf'), float('inf') # 兩次交易的成本 (最低買入價格)
        profit1, profit2 = 0, 0 # 發生一次或兩次交易後，最大的獲利
        # profit1 是只有發生一次交易的獲利
        # profit2 是發生兩次交易後的獲利 (不是單獨第二次交易的獲利)
        for price in prices:
            cost1 = min(cost1, price) # 找出第一次交易的最低價格
            profit1 = max(profit1, price - cost1)

            # profit2 = (sell_price2 - buy_price2) + (sell_price1 - buy_price1)
            #         = sell_price2 - buy_price2 + profit1
            #         = sell_price2 - (buy_price2 - profit1)
            #         = sell_price2 - cost2
            # 所以 cost2 = buy_price2 - profit1
            
            cost2 = min(cost2, price - profit1)
            profit2 = max(profit2, price - cost2)

        return profit2
