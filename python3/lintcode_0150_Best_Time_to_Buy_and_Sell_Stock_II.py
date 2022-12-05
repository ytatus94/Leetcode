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

        # 因為可以買賣無限次，每次手上只能持有一股
        # 昨天買，明天賣可以等價於昨天買，今天賣掉之後再買入，明天再賣
        # 所以只要 prices[i] > prices[i-1] 那就有 profit

        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
