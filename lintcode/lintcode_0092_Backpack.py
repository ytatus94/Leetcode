# 背包型 DP, 最值型 DP
# 轉移方程
#   f[i][w] = f[i-1][w] or f[i-1][w-a[i-1]]
#   要看前 i 個物品能不能拼出重量 w (w = 0 ~ 最大承重)
#   f[i-1][w] = 用前 i 個物品已經能拼出重量 w
#   f[i-1][w-a[i-1] = 用前 i 個物品能拼出 w-a[i-1] 再加上第 i 個物品 (index = i-1) 的重量 a[i-1] 就能拼出 w
# 初始條件
# f[0][0] = True 前 0 個物品能拼出重量 0
# f[0][w>0] = False 前 0 個物品不能拼出任何重量 > 0 的
# TC = O(MN) = 計算步數, SC = O(MN) = 數組大小，可以優化成 O(M)

from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        if a is None:
            return 0
        n = len(a)
        if n == 0:
            return 0

        # 建立一個數組紀錄前 i 個物品可以拼出的所有種可能重量 w
        # f[i][w=0~m] = 前 i 個物品能否拼出重量 w, w 從 0 ~ m
        f = [[False for j in range(m + 1)] for i in range(n + 1)]

        # 初始化
        f[0][0] = True # 前 0 個物品可以拼出重量 0
        for i in range(1, m + 1):
            f[0][i] = False # 前 0 個物品不可能拼出大於 0 的重量
        
        # 要由前 i 個物品拼出重量 j 有兩種可能
        # 1. 前 i-1 個物品已經能拼出重量 j
        # 2. 前 i-1 個物品只能拼出 j - A[i-1], 再加上第 i 個物品的重量 A[i-1] 就能拼出重量 j
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                f[i][j] = f[i - 1][j] # 前 i-1 個物品已經能拼出重量 j
                if j >= a[i - 1]:
                    f[i][j] |= f[i - 1][j - a[i - 1]]

        results = 0
        for i in range(m, -1, -1):
            if f[n][i] == True:
                results = i
                break

        return results

    
# 如果要把背包內的物品印出來
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        if a is None:
            return 0
        n = len(a)
        if n == 0:
            return 0

        # 建立一個數組紀錄前 i 個物品可以拼出的所有種可能重量 w
        # f[i][w=0~m] = 前 i 個物品能否拼出重量 w, w 從 0 ~ m
        f = [[False for j in range(m + 1)] for i in range(n + 1)]

        # 把放到背包的物品印出來
        pi = [[0 for j in range(m + 1)] for i in range(n + 1)]
        # pi[i][j] = 0: 不用第 i 個
        # pi[i][j] = 1: 用第 i 個

        # 初始化
        f[0][0] = True # 前 0 個物品可以拼出重量 0
        for i in range(1, m + 1):
            f[0][i] = False # 前 0 個物品不可能拼出大於 0 的重量
        
        # 要由前 i 個物品拼出重量 j 有兩種可能
        # 1. 前 i-1 個物品已經能拼出重量 j
        # 2. 前 i-1 個物品只能拼出 j - A[i-1], 再加上第 i 個物品的重量 A[i-1] 就能拼出重量 j
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                f[i][j] = f[i - 1][j] # 前 i-1 個物品已經能拼出重量 j
                # pi[i][j] = 0
                if j >= a[i - 1]:
                    if f[i - 1][j - a[i - 1]]: # 這時候會用到第 i 個
                        pi[i][j] = 1
                    f[i][j] |= f[i - 1][j - a[i - 1]]

        results = 0
        for i in range(m, -1, -1):
            if f[n][i] == True:
                results = i
                break

        print('Put the following items in the backpack')
        i = results
        for j in range(n, 0, -1):
            if pi[j][i] == 1:
                print(a[j - 1])
                i -= a[j - 1]

        return results

# 方法2
from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n_items = len(a)

        # 先想成要看能不能用 n 個物品組成 size = 0 ~ m
        # 然後再找 n 個物品能組成的最大 size

        # dp[i][j] = 能不能用前 i 個物品組成 size=j
        dp = [[False for j in range(m + 1)] for i in range(n_items + 1)]
        dp[0][0] = True # 用前 0 個物品組成 size=0，當然行

        for i in range(1, n_items + 1):
            for j in range(0, m + 1):
                dp[i][j] = dp[i - 1][j] # 用前 i-1 個物品就能組成 size=j
                if j >= a[i - 1]:
                    # 如果前 i-1 個物品只能拼成 size=j-a[i-1]
                    # 加上第 i 個物品的 size=a[i-1] 就能拼成 size=j
                    dp[i][j] = dp[i][j] or dp[i - 1][j - a[i - 1]]

        # 要看全部物品能拼成的最大 size
        # 全部物品 --> 只看 n_items row
        # 要找最大 size --> 從後面開始往前找
        max_size = 0
        for j in range(m, -1, -1):
            if dp[n_items][j] == True:
                max_size = j
                
                return max_size
