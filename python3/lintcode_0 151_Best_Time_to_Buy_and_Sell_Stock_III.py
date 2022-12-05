# 序列型 DP, 最值型 DP
# 轉移方程:
#   分成五個狀態: 1 (沒有股票) --> 2 (第一次買入並持有股票) ---> 3 (第一次賣出，沒有股票了) --> 4 (第二次買入並持有股票) --> 5 (第二次賣出，沒有股票了)
#   case 1, 3, 5: 沒有股票 f[i][j] = max( f[i-1][j], f[i-1][j-1]+p(i-1)-p(i-2) )
#                                = max(昨天就沒股票, 昨天有股票今天賣掉)
#   case 2, 4: 有股票 f[i][j] = max( f[i-1][j]+p(i-1)-p(i-2), f[i-1][j-1])
#                           = max(昨天有股票今天持有會持續增值, 昨天沒股票今天買入) 
#   f[i][j] = 前 i 天並處於 j 狀態的最大獲利
# 初始條件:
#   f[0][1] = 0 前 0 天賺 0 元, f[0][2...5] = -inf 前 0 天不可能是狀態 2~5
# TC = O(N), SC = O(N), 可以用滾動數組優化成 O(1)

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
        # of the first i days and status
        f = [[0 for i in range(5 + 1)] for j in range(n + 1)]
        # There are five status (3 cases no stock and 2 cases have stock)
        # 1. before 1st buy: no stock
        # 2. 1st buy and keep it: have stock on hand
        # 3. 1st sell: no stock
        # 4. 2nd buy and keep it: have stock on hand
        # 5. 2nd sell: no stock
        # f[i][j] = the maximum profit on the first i days when status is j
        # when no stock (case 1, 3, 5)
        # f[i][j] = max( f[i-1][j], f[i-1][j-1]+(P(i-1)-P(i-2)) )
        # f[i-1][j]: day index=i-2 no stock, in the same status j
        # f[i-1][j-1] + (P(i-1)-P(i-2)): day index=i-2 has stock, 
        # in status j-1, and sell on day index=i-1
        # when have stock on hand (case 2, 4)
        # f[i][j] = max( f[i-1][j]+(P(i-1)-P(i-2)), f[i-1][j-1] )
        # f[i-1][j]+(P(i-1)-P(i-2)): day index=i-2 has stock, 
        # in the same status j, keep it and earn some profit (but not sell it yet)
        # f[i-1][j-1]: day index=i-2 no stock, and buy on day index=i-1

        # initial condition: the first 0 day
        f[0][1] = 0 # first 0 day, no stock, in status 1
        for i in range(2, 6):
            # it is impossible to have f[0][2] to f[0][5]
            # so set it to -infinity
            f[0][i] = float('-inf') 

        for i in range(1, n + 1):
            # case 1, 3, 5
            # f[i][j] = max( f[i-1][j], f[i-1][j-1]+(P(i-1)-P(i-2)) )
            for j in range(1, 6, 2):
                f[i][j] = f[i - 1][j]
                if i >= 2 and j > 1:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            # case 2, 4
            # f[i][j] = max( f[i-1][j]+(P(i-1)-P(i-2)), f[i-1][j-1] )
            for j in range(2, 6, 2):
                f[i][j] = f[i - 1][j - 1]
                if i >= 2: # 也要 j > 1, 但是 j 從 2 開始所以一定成立
                    f[i][j] = max(f[i][j], f[i - 1][j] + prices[i - 1] - prices[i - 2])

        # the maximum profit is selling all stocks and no stock on hand
        return max(f[n][1], max(f[n][3], f[n][5]))                
