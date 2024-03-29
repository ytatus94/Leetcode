# 雙序列型 DP, 計數型 DP
# 轉移方程
#   f[i][j] = f[i-1][j-1]|A[i-1]=B[j-1] + f[i-1][j]
# 初始條件
#   f[i][0] = 1 (i = 0, 1, 2, ..., m)
#   f[0][j] = 0 (j = 1, 2, ..., n)
# TC = O(MN), SC = O(MN) 可以用滾動數組優化成 O(N)

class Solution:
    """
    @param s: A string
    @param t: A string
    @return: Count the number of distinct subsequences
    """
    def num_distinct(self, s: str, t: str) -> int:
        # write your code here
        m = len(s)
        n = len(t)

        # f[i][j] = t 的前 j 個字元在 s 的前 i 個字元中出現了幾次
        f = [[0 for j in range(n + 1)]for i in range(m + 1)]
        # initial conditions
        # f[i][0] = 1 s 不空 t 是空，那 t 在 s 中出現 1 次
        # f[0][j>0] = 0 s 是空 t 不空，那 t 在 s 中出現 0 次

        # 要看的是 s 裡面有多少個子字串是 t 所以 t 是不動的
        # 可以想成是 t 在 s 中出現了幾次
        # case1. s[m-1] = t[n-1]
        # 看 t[n-2] 在 s[m-2] 中出現幾次: f[i][j] = f[i-1][j-1]
        # case2. s[m-1] != t[n-1]
        # 看 t[n-1] 在 s[m-2] 中出現幾次: f[i][j] = f[i-1][j]
        # 歸納出 f[i][j] = f[i-1][j-1]|最後一個字元相同 + f[i-1][j]
        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0: # t 是空串
                    f[i][j] = 1 # initial conditions
                    continue
                
                # j > 0
                if i == 0: # s 是空串
                    f[i][j] = 0 # initial conditions
                    continue
                
                # i > 0 && j > 0
                # 最後一個字元不相等時
                f[i][j] = f[i - 1][j]
                
                # 最後一個字元相等時
                if s[i - 1] == t[j - 1]:
                    f[i][j] += f[i - 1][j - 1]

        return f[m][n]

# 用滾動數組
class Solution:
    """
    @param s: A string
    @param t: A string
    @return: Count the number of distinct subsequences
    """
    def num_distinct(self, s: str, t: str) -> int:
        # write your code here
        m = len(s)
        n = len(t)

        # 滾動數組
        old, new = None, 0

        # 有滾動數組的時候只要開二維矩陣
        # i-1 --> old, i --> new
        f = [[0 for j in range(n + 1)]for i in range(2)]
        # initial conditions
        # f[i][0] = 1 s 不空 t 是空，那 t 在 s 中出現 1 次
        # f[0][j>0] = 0 s 是空 t 不空，那 t 在 s 中出現 0 次

        # 要看的是 s 裡面有多少個子字串是 t 所以 t 是不動的
        # 可以想成是 t 在 s 中出現了幾次
        # case1. s[m-1] = t[n-1]
        # 看 t[n-2] 在 s[m-2] 中出現幾次: f[i][j] = f[i-1][j-1]
        # case2. s[m-1] != t[n-1]
        # 看 t[n-1] 在 s[m-2] 中出現幾次: f[i][j] = f[i-1][j]
        # 歸納出 f[i][j] = f[i-1][j-1]|最後一個字元相同 + f[i-1][j]

        for i in range(m + 1):
            # 滾動數組進入 i 迴圈就要互換 old, new
            old = new
            new = 1 - new
            for j in range(n + 1):
                if j == 0: # t 是空串
                    f[new][j] = 1 # initial conditions
                    continue
                
                # j > 0
                if i == 0: # s 是空串
                    f[new][j] = 0 # initial conditions
                    continue
                
                # i > 0 && j > 0
                f[new][j] = f[old][j]

                if s[i - 1] == t[j - 1]:
                    f[new][j] += f[old][j - 1]

        return f[new][n]
