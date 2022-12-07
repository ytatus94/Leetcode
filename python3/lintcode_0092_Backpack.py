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
