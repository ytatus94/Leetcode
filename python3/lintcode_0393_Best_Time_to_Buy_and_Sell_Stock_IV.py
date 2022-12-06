# 序列型 DP, 最值型 DP
# 轉移方程:
#  第 k 次交易後，狀態是 2k+1 (畫圖列出來就看得出規律)
#   case 1: 沒有股票，狀態是奇數
#   f[i][j] = max( f[i-1][j], f[i-1][j-1]+(P[i-1]-P[i-2] )
#   = max( 昨天沒股票, 昨天有股票今天賣掉 )
#   case 2: 手上有股票，狀態是偶數
#   f[i][j] = max( f[i-1][j]+(P[i-1]-P[i-2]), f[i-1][j-1] )
#   = max( 昨天手上有股票今天增值, 昨天沒股票今天買入 )
# 初始條件:
#   f[0][1] = 0, f[1...2k+1] = -inf
# TC = O(NK), SC = O(NK) 用滾動數組可以優化成 O(K)

# 方法1:
from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def max_profit(self, k: int, prices: List[int]) -> int:
        # write your code here
        if prices is None:
            return 0
        n = len(prices)
        if n == 0:
            return 0

        # This problem is the combination of 
        # Best Time to Buy and Sell Stock II (when k > N/2)and
        # Best Time to Buy and Sell Stock III (when k = 2).

        # If k > N/2, then we can buy more than one time in a day
        # 1st buy 1st sell and then 2nd buy 2nd sell ... nst buy nst sell in a day
        # This can be treated as 1st buy and nst sell only

        # Best Time to Buy and Sell Stock II
        if k > n / 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # Similar to Best Time to Buy and Sell Stock III
        # After k sell, the status becomes 2k+1
        # all odd status are no stock, and all even status are having stocks
        f = [[0 for j in range(2 * k + 2)] for i in range(n + 1)]
        
        # initial conditions
        f[0][1] = 0
        for i in range(2, 2 * k + 2): # because we need to consider 0, we use 2K+2
            f[0][i] = float('-inf')

        for i in range(1, n + 1):
            # odd status: 1, 3, 5,..., 2k+1, no stock
            for j in range(1, 2 * k + 2, 2):
                f[i][j] = f[i - 1][j]
                if i >= 2 and j > 1:
                    f[i][j] = max(
                        f[i][j],
                        f[i - 1][j - 1] + prices[i - 1] - prices[i - 2]
                    )

            # even status: 2, 4, 6,...,2k, have stocks
            for j in range(2, 2 * k + 1, 2):
                f[i][j] = f[i - 1][j - 1]
                if i >= 2:
                    f[i][j] = max(
                        f[i][j],
                        f[i - 1][j] + prices[i - 1] - prices[i - 2]
                    )
        
        profit = 0
        for i in range(1, 2 * k + 2, 2):
            profit = max(profit, f[n][i])

        return profit

# 方法2: 用滾動數組
from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def max_profit(self, k: int, prices: List[int]) -> int:
        # write your code here
        if prices is None:
            return 0
        n = len(prices)
        if n == 0:
            return 0

        # This problem is the combination of 
        # Best Time to Buy and Sell Stock II (when k > N/2)and
        # Best Time to Buy and Sell Stock III (when k = 2).

        # If k > N/2, then we can buy more than one time in a day
        # 1st buy 1st sell and then 2nd buy 2nd sell ... nst buy nst sell in a day
        # This can be treated as 1st buy and nst sell only

        # Best Time to Buy and Sell Stock II
        if k >= n / 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # Similar to Best Time to Buy and Sell Stock III
        # After k sell, the status becomes 2k+1
        # all odd status are no stock, and all even status are having stocks
        f = [[0 for j in range(2 * k + 2)] for i in range(n + 1)]
        
        # 用滾動數組
        old = None
        new = 0

        # initial conditions
        f[new][1] = 0
        for i in range(2, 2 * k + 2): # because we need to consider 0, we use 2K+2
            f[new][i] = float('-inf')

        for i in range(1, n + 1):
            # 用滾動數組時
            # f[i] -> new
            # f[i-1] -> old
            old = new
            new = 1 - new
            # odd status: 1, 3, 5,..., 2k+1, no stock
            for j in range(1, 2 * k + 2, 2):
                f[new][j] = f[old][j]
                if i >= 2 and j > 1:
                    f[new][j] = max(
                        f[new][j],
                        f[old][j - 1] + prices[i - 1] - prices[i - 2]
                    )

            # even status: 2, 4, 6,...,2k, have stocks
            for j in range(2, 2 * k + 1, 2):
                f[new][j] = f[old][j - 1]
                if i >= 2:
                    f[new][j] = max(
                        f[new][j],
                        f[old][j] + prices[i - 1] - prices[i - 2]
                    )
        
        profit = 0
        for i in range(1, 2 * k + 2, 2):
            profit = max(profit, f[new][i])

        return profit

