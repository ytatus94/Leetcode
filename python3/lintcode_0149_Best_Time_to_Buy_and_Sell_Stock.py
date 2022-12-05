# 座標型 DP, 最值型 DP
# 轉移方程:
#   f[i] = min(f[i], prices[i] - prices[j])
#   f[i] = 第 i 天賣的最大獲利
# 初始條件:
#   f[0] = 0, f[1] = 0 第一天買又第一天賣，賺到 0 元
# 用兩個 for loops: TC = O(N^2) 會超時, SC = O(N) 

# 方法 1: 兩個 for loops 會超時
from typing import (
    List,
)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        # write your code here
        if prices is None:
            return 0
        n = len(prices)
        if n == 0:
            return 0

        # Create an array to save the maximum profit
        # f[i] = maximum profit on day i
        f = [0 for i in range(n + 1)]

        # initial condition
        f[0] = 0
        f[1] = 0 # buy on day 1 and sell on day 1, profit = 0

        for i in range(2, n + 1): # sell on day i
            for j in range(1, i): # buy on day j
                f[i] = max(f[i], prices[i - 1] - prices[j - 1])

        return max(f)
        
# 方法 2: 時刻保存第 i 天之前的最小值
from typing import (
    List,
)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        # write your code here
        if prices is None:
            return 0
        n = len(prices)
        if n == 0:
            return 0

        max_profit = 0
        lowest_price = prices[0]

        for i in range(1, n): # sell on day i
            print(i)
            max_profit = max(max_profit, prices[i] - lowest_price)
            lowest_price = min(prices[i], lowest_price)

        return max_profit
