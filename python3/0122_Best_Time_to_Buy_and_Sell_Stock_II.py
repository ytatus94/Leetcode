class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        daily_profit = [0 for i in range(len(prices))]

        # 因為每天手上最多只能持有一股，所以今天買明天賣，計算每日獲利
        # ex: (第 i 天買，第 i+3 天賣) 和 (第 i 天買，第 i+1 天賣，第 i+1 天買，第 i+2 天賣，第 i+2 天買，第 i+3 天賣) 獲利是一樣的
        for i in range(1, len(prices)):
            daily_profit[i] = prices[i] - prices[i - 1]

        total_profit = 0
        for i in daily_profit:
            if i > 0: # 只看獲利的部分，虧損用不管
                total_profit += i

        return total_profit

      # 方法 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
