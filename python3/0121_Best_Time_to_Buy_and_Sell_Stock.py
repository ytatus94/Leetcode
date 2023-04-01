class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        lowest_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > lowest_price: # 有獲利
                max_profit = max(max_profit, prices[i] - lowest_price)

            # 今天價格比最低價還低，那對未來的日子來說，今天就是最低價，所以要記錄下來
            if prices[i] < lowest_price:
                lowest_price = prices[i]
        return max_profit


    # 會超時
    # def maxProfit(self, prices: List[int]) -> int:
    #     if prices is None or len(prices) == 0:
    #         return 0

    #     max_profit = 0
    #     for i in range(1, len(prices)): # i 是賣出
    #         for j in range(i): # j 是買入 (往前看，所以 j < i)
    #             if prices[i] > prices[j]:
    #                 profit = prices[i] - prices[j]
    #                 max_profit = max(profit, max_profit)
    #     return max_profit

