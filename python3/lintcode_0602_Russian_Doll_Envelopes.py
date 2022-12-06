# 最長序列型 DP (座標型), 計數型 DP
# 轉移方程:
#   f[i] = max( 1, f[j]+1|Ej < Ei )
#   f[i] = 以信封 i 為最外層，所能套的信封總數 (包含 i 自己)
# 初始條件: 沒有初始條件

# 方法1: TC = O(N^2), SC = O(N) 會超時
from typing import (
    List,
)

class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def max_envelopes(self, envelopes: List[List[int]]) -> int:
        # write your code here
        if envelopes is None:
            return 0
        n = len(envelopes)
        if n == 0:
            return 0

        # 要先把 envelops 依照長度和寬度排序
        env = sorted(envelopes, key=lambda x: (x[0], x[1]))
        
        # 建立一個數組儲存第 i 個信封能套的最大數目
        # f[i] = 算到信封 i 時最多能套多少個 (包含 i 自己)
        f = [0 for i in range(n)] # 座標型 DP 只要開到 n

        # 沒有初始條件

        results = 0
        for i in range(n):
            # case 1
            f[i] = 1 # 如果不能套任何其他信封，那只有自己一個

            # case 2
            for j in range(i):
                if env[i][0] > env[j][0] and env[i][1] > env[j][1]:
                    f[i] = max(f[i], f[j] + 1)
            results = max(results, f[i])

        return results
