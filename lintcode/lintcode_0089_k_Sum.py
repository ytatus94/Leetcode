# 背包型 DP, 計數型 DP
# 轉移方程
#   f[i][k][s] = f[i-1][k][s] + f[i-1][k-1][s-A[i-1]]|k>=1 and s>=A[i-1]
#   f[i][k][s] 從前 i 個數中選出 k 個使得和是 s 的方法數
#   A[i-1] 不進背包 f[i-1][k][s]
#   A[i-1] 進背包 f[i-1][k-1][s-A[i-1]]|k>=1 and s>=A[i-1]
# 初始條件
#   f[0][0][0] = 1
#   f[0][0][s] = 0
#   f[0][j>0][s>0] = 0
# TC = O(N*K*target), SC = O(N*K*target) 可以用滾動數組優化成 O(K*target)

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        # write your code here
        n = len(a)
        if n == 0:
            return

        # f[i][j][s] = 前 i 個物品選出 j 個，使得和是 s 的方法數
        f = [[[0 for s in range(target + 1)] for j in range(k + 1)] for i in range(n + 1)]
        
        # initial conditions
        f[0][0][0] = 1 # 從前 0 個物品選出 0 個，使得和是 1 的方法數就是一種
        # f[0][j>0][0] = 0
        # f[0][0][s>0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                for s in range(target + 1):
                    f[i][j][s] = f[i - 1][j][s]
                    if j > 0 and s >= a[i - 1]:
                        f[i][j][s] += f[i - 1][j - 1][s - a[i - 1]]

        return f[n][k][target] 
