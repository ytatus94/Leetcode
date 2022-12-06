# 最長序列型 DP, 計數型
# 轉移方程:
#   f[i] = max(1, f[j]+1|(i>j&&a[i]>a[j]) )
# 初始條件: 沒有初始條件
# TC = O(N^2), SC = O(N)

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        # write your code here
        if nums is None:
            return 0
        n = len(nums)
        if n == 0:
            return 0

        # Create an array
        f = [0 for i in range(n)]
        # f[i] means the LIS ending with a[i]

        # No initial condition

        for i in range(n):
            f[i] = 1 # 如果前面的數都比 a[i] 大，那子序列就是 a[i] 自己
            for j in range(i): # 枚舉 a[i] 前面的所有的數目
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
