# 背包型 DP, DP
# 轉移方程:
# f[i][w] = max_{k>=0}( f[i-1][w-k*a[i-1]]+k*v[i-1])
#         = 用前 i 種物品拼出重量 w 時的最大價值
# backpack 2 是 k=0, 1 的特例
# 經過整理後可以改寫成 f[i][w] = max( f[i-1][w], f[i][w-a[i-1]]+v[i-1] )
# 初始條件
# f[0][0] = 0 前 0 種物品拼出 w=0 的最大價值是 0
# f[0][w>0] = -1 拼不出來用 -1
# TC = O(MN), SC = O(MN) 可以空間優化成 O(M)

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    def back_pack_i_i_i(self, a: List[int], v: List[int], m: int) -> int:
        # write your code here
        if a is None:
            return 0
        n = len(a)
        if n == 0:
            return 0

        # 當物品能有無限多個的時候，就只能用種類計算
        # f[i][w] = 前 i 種物品組成重量 w 時的最大價值
        # = max_{0<=k}(f[i-1][w-k*A[i-1]]+k*V[i-1])
        # 前 i-1 種物品拼出 w-k*A[i-1] 的最大價值，加上第 i 種物品有 k 個的價值
        # Backpack II 是 k = 0, 1 的特例
        # f[i][w] = max(f[i-1][w], f[i-1][w-A[i-1]]+V[i-1], f[i-1][w-2*A[i-1]]+2*V[i-1],...)
        # = max(f[i-1][w], f[i][w-A[i-1]]+V[i-1])

        f = [[-1 for w in range(m + 1)] for i in range(n + 1)]
        # initial condition
        f[0][0] = 0

        for i in range(1, n + 1):
            for w in range(0, m + 1):
                f[i][w] = f[i - 1][w]
                if w - a[i - 1] >= 0 and f[i][w - a[i - 1]] != -1: # 注意這邊看的是 f[i], backpack 2 看的是 i-1
                    f[i][w] = max(f[i][w], f[i][w - a[i - 1]] + v[i - 1])

        return max(f[n])

# 空間優化
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    def back_pack_i_i_i(self, a: List[int], v: List[int], m: int) -> int:
        # write your code here
        if a is None:
            return 0
        n = len(a)
        if n == 0:
            return 0

        # 當物品能有無限多個的時候，就只能用種類計算
        # f[i][w] = 前 i 種物品組成重量 w 時的最大價值
        # = max_{0<=k}(f[i-1][w-k*A[i-1]]+k*V[i-1])
        # 前 i-1 種物品拼出 w-k*A[i-1] 的最大價值，加上第 i 種物品有 k 個的價值
        # Backpack II 是 k = 0, 1 的特例
        # f[i][w] = max(f[i-1][w], f[i-1][w-A[i-1]]+V[i-1], f[i-1][w-2*A[i-1]]+2*V[i-1],...)
        # = max(f[i-1][w], f[i][w-A[i-1]]+V[i-1])

        f = [-1 for w in range(m + 1)]
        # initial condition
        f[0] = 0

        for i in range(1, n + 1):
            for w in range(0, m + 1):
                if w - a[i - 1] >= 0 and f[w - a[i - 1]] != -1: # 注意這邊看的是 f[i], backpack 2 看的是 i-1
                    f[w] = max(f[w], f[w - a[i - 1]] + v[i - 1])

        return max(f)
