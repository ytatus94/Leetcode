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
                        pi[i] = j # 這裡記錄的是第 i 個元素的值比第 j 個元素的值大

            results = max(results, f[i])
            if f[i] == results: # 有更新了就要記錄下來
                p = i # 最長子序列是哪個 index 做結尾

        seq = [0 for i in range(results)] # 印出來
        for i in range(results - 1, -1, -1):
            seq[i] = nums[p]
            p = pi[p]

        return results
    
# 用二分法 TC = O(N logN)
# 不過我不是很懂

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

        # 有可能有好幾個 a[x] 有相同的 f 值
        # 例如 a[0]=5, a[1]=1, 但是 f[0] = f[1] = 1
        # 這時候 b[1] = a[1] = 1 
        # b[i] = 當 f[x] = i 的時候，最小的那個 a[x]
        # b 的下標就是 f 值，b[下標]=a[x]
        b = [float('-inf') for i in range(n + 1)]

        top = 0
        j = 0

        for i in range(n):
            start = 0
            end = top
            while (start <= end):
                mid = (start + end) // 2
                if b[mid] < nums[i]:
                    j = mid
                    start = mid + 1
                else:
                    end = mid - 1
                    
            # 因為找到了相同 f 值 (f=j) 卻比 nums[i] 還小的 nums[x]
            # 所以可以放心的把 nums[i] 放到 b[j + 1]
            b[j + 1] = nums[i]
            if j + 1 > top:
                top = j + 1
        # b[0], b[1],...,b[top]
        return top
