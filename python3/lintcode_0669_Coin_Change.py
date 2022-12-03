# TC = O(總步數 x 硬幣面額數)
# 總步數其實就是 Target 的大小
from typing import (
    List,
)

import sys

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coin_change(self, coins: List[int], amount: int) -> int:
        # write your code here
        # 開一個數組, 長度是 amount
        # f[X] = 需要"多少枚" coins 來拼出 X
        f = [sys.maxsize] * (amount + 1) # 因為要求"最少"多少枚, 所以初始化成 max value
        
        # 初始化
        f[0] = 0 # 需要 0 枚 coin 拼出 0

        for i in range(amount + 1):
            for coin in coins: # coin 是一枚硬幣的面額
                if i >= coin and f[i - coin] != sys.maxsize:
                    f[i]= min(f[i], f[i - coin] + 1)
        
        if f[amount] == sys.maxsize:
            return -1
        else:
            return f[amount]
