# 最長序列型 DP (座標型), 計數型 DP
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
        f = [0 for i in range(n)] # 因為是座標型，只要開 n 就可以了
        # f[i] means the LIS ending with a[i]

        # No initial condition

        for i in range(n):
            # case 1: 只有自己
            f[i] = 1 # 如果前面的數都比 a[i] 大，那子序列就是 a[i] 自己
            
            # case 2: a[i] 是序列的最後一個數
            for j in range(i): # 枚舉 a[i] 前面的所有的數目
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)

    
# 把最長子序列印出來 (要會！)
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

        # 開一個數組紀錄最長子序列是要選哪一個 index
        pi = [0 for i in range(n)]
        p = 0

        results = 0

        for i in range(n):
            f[i] = 1 # 如果前面的數都比 a[i] 大，那子序列就是 a[i] 自己
            pi[i] = -1 # 表示只有自己
            for j in range(i): # 枚舉 a[i] 前面的所有的數目
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
                    if f[i] == f[j] + 1: # 有更新了就要記錄下來
                        pi[i] = j

            results = max(results, f[i])
            if f[i] == results: # 有更新了就要記錄下來
                p = i # 最長子序列是哪個 index 做結尾

        seq = [0 for i in range(results)] # 印出來
        for i in range(results - 1, -1, -1):
            seq[i] = nums[p]
            p = pi[p]

        return results
    
