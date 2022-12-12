# 背包型 DP, 最值型 DP
# 轉移方程
#   f[i][w] = 前 i 個物品拼出 w 時的最大價值，-1 表示拼不出來
#   = max(f[i-1][w], f[i-1][w-a[i-1]]+v[i-1])
# 可以是由前 i-1 個物品拼出重量 w 時的最大價值
# 或是前 i-1 個物品拼出重量 w-a[i-1] 時的最大價值，再加上第 i 個物品 (index=i-1) 的價值 v[i-1]
# 初始條件
# f[0][0] = 0
# f[0][1...m] = -1
# TC = O(MN) = 計算步數, SC = O(M) = 數組大小

from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        # write your code here
        if a is None:
            return 0

        n = len(a)
        if n == 0:
            return 0

        # f[i][w] = 前 i 個物品拼出重量 w 時的最大價值, 如果不能拼出重量 w, 那就是 -1
        # = max(f[i-1][w],  f[i-1][w-A[i-1]] + v[i-1])
        # 拼出 w 時的最大價值是由前 i-1 個物品拼出來的
        # 或者是前 i-1 個物品只拼出 w-A[i-1] 的最大價值加上第 i (index=i-1) 個物品的價值
        f = [[-1 for w in range(m + 1)] for i in range(n + 1)]
        # initial condition
        f[0][0] = 0

        for i in range(1, n + 1):
            for w in range(m + 1):
                f[i][w] = f[i - 1][w] # 前 i-1 個物品拼出 w 時的最大價值
                if w >= a[i - 1] and f[i - 1][w - a[i - 1]] != -1:
                    f[i][w] = max(f[i][w], f[i - 1][w - a[i - 1]] + v[i-1])
        
        # 找出用前 n 個物品拼出的最大價值
        return max(f[n])
