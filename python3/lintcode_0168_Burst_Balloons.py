# 區間型 DP
# 轉移方程
# f[i][j] = 扎破 i+1 到 j-1 的氣球能得到的最大金幣數
# = max_{i<k<j}( f[i][k] + f[k][j] + A[i]*A[k]*A[j] )
# i, j 是邊界氣球，不能扎破
# 分成獨立的兩段，先看 i,k 之間能得到的最大金幣數，在看 j,k 之間能得到的最大金幣數，最後扎破 k 
# 初始條件
# f[0][1] = f[1][2] = ... = 0 邊界氣球相鄰，中間沒有能扎破的氣球
# TC = O(N^3), SC = O(N^2)

from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def max_coins(self, nums: List[int]) -> int:
        # write your code here
        if nums is None:
            return 0
        n = len(nums)
        if n == 0:
            return 0

        # 要在 0 的前面和 n-1 的後面各加上一個當作邊界的氣球，並且值是 1
        new_nums = [1] + nums + [1]
        m = len(new_nums)

        # create f[i][j] = maximum coins between i and j where i, j are boundries
        # 只有 i+1 到 j-1 的氣球能被扎破
        f = [[float('-inf') for j in range(m)] for i in range(m)]
        
        # initial condition (length = 2)
        for i in range(m - 1):
            f[i][i + 1] = 0 # 中間沒有氣球能扎破，所以是 0 coin
        
        print(nums)
        print(n)
        print(new_nums)
        print(m)
        print(f)

        # 要有中間能扎破的氣球，左右兩邊的氣球是邊界，不能扎
        # 那最少長度要從 3 開始，最長是 m (最後一個氣球是邊界不能扎)
        for length in range(3, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                # [i] i+1, i+2, ..., k, ..., j-2, j-1, [j]
                # [i], [j] 表示不能扎, k 是 i+1 到 j-1 中最後一個被扎破的氣球
                # 看子問題時，k 也變成邊界，所以要看所有可能的 k
                for k in range(i + i, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + new_nums[i] * new_nums[k] * new_nums[j])
        print(f)
        return f[0][m - 1]
