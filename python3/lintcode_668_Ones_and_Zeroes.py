from typing import (
    List,
)

class Solution:
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """
    def find_max_form(self, strs: List[str], m: int, n: int) -> int:
        # write your code here
        t = len(strs)
        if t == 0:
            return 0

        # f[i][j][k] = 前 i 個 01 串裡面，有 j 個 0 和 k 個 1 來組成
        f = [[[0 for k in range(n + 1)] for j in range(m + 1)]for i in range(t + 1)]

        # 相當於背包問題，要考慮最後一個物品進不進背包
        # 不進: m 個 0 和 n 個 1 就用來構成前 t-1 個 01 串裡
        # 進: 第 t 個物品 (index=t-1) 有 a0 個 0 和 a1 個 1
        # --> f[i-1][j][k]
        # 所以前 t-1 個物品就由 m-a0 個 0 和 n-a1 個 1 來構成
        # --> f[t-1][m-a0][n-a1] + 1 注意 m>=a0, n>=a1
        # f[i][j][k] = max(f[i-1][j][k], f[i-1][m-a0][n-a1])
        
        # initla condition
        # f[0][m][n] = 0 # 空串不能由 m 個 0 和 n 個 1 來組成

        for i in range(1, t + 1):
            # 計算第 i 個字串 strs[i-1] 中有多少個 0 和 1
            a0, a1 = 0, 0
            for j in range(len(strs[i - 1])): # 注意要 i > 0
                if strs[i - 1] == '0':
                    a0 += 1
                else:
                    a1 += 1

            for j in range(m + 1):
                for k in range(n + 1):
                    # 最後一個字串不進背包
                    f[i][j][k] = f[i - 1][j][k] 

                    # 最後一個字串不進背包
                    if j >= a0 and k >= a1:
                        f[i][j][k] = max(f[i][j][k], f[i - 1][j - a0][k - a1] + 1)

        return f[t][m][n]
