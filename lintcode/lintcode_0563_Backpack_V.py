# 背包型 DP，計數型 DP
# 轉移方程
#   f[i][w] = f[i-1][w] + f[i-1][w-A[i-1]]
#   f[i][w] = 前 i 個物品有多少種方式能拼出 w
#           = 前 i-1 個物品拼出 w 的方式 + 前 i-1 個物品拼出 w-A[i-1] 的方式
# 初始條件
# f[0][0] = 1 前 0 個物品有 1 種方式拼出 0
# f[0][w>0] = 前 0 個物品不可能拼出比 0 大的 w
# TC = O(N * target) = 計算步數, SC = O(target) = 數組大小

from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def back_pack_v(self, nums: List[int], target: int) -> int:
        # write your code here
        if nums is None:
            return 0
        n = len(nums)
        if n == 0:
            return 0

        # 開一個數組
        # f[i][w] = 前 i 個物品有幾種方式能拼出 w (w=0~target)
        # 本來是要開 2-dim 的數組，但是這一題可以開 1-dim
        f = [0 for i in range(target + 1)]

        # 初始條件
        f[0] = 1 # f[0][0] = 前 0 個物品有 1 種方式拼出 0
        for i in range(1, target + 1):
            f[i] = 0 # f[0][w>0] = 前 0 個物品無法拼出 w

        for i in range(1, n + 1):
            for j in range(target, -1, -1): # 開 1-d 數組的時候，要到著來
                if j >= nums[i - 1]:
                    f[j] += f[j - nums[i - 1]]

        return f[target]
