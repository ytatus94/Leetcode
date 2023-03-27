# 最值型 DP
# 轉移方程:
#   最大乘積 f[j] = max( a[j], max( a[j]*f[j-1], a[j]*g[j-1])|j>0 )
#   最小乘積 g[j] = min( a[j], min( a[j]*f[j-1], a[j]*g[j-1])|j>0 )
#   f[j] = 以 a[j] 結尾的連續子序列的最大乘積
#   case 1) a[j]: 當子序列本身只有 a[j] 自己
#   case 2) 以 a[j-1] 結尾的連續子序列最大乘積 f[j-1] 或最小乘積 g[j-1] 再乘上 a[j]
# 初始條件: 沒有初始條件
# TC = O(N) SC = O(N) 

from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def max_product(self, nums: List[int]) -> int:
        # write your code here
        if len(nums) == 1:
            return nums[0]

        # 因為 array 裡面有正有負，需要紀錄子序列乘積中最大的和最小的值
        # 因為負數是越負的越小，乘積如果是負數，再乘上一個負數，就變成正數了
        f = [-1 * sys.maxsize for i in range(len(nums))] # 保存乘積的最大值
        g = [sys.maxsize for i in range(len(nums))] # 保存乘積的最小值

        # 因為子序列的第一個數的位置可能會變來變去，所以 f 和 g 沒有初始值

        for i in range(len(nums)):
            f[i] = nums[i]
            g[i] = nums[i]
            if i - 1 >= 0:
                # 看看是當前這個數比較大，還是前面的最大乘積或最小乘積乘以當前的數後比較大
                f[i] = max(f[i], max(f[i - 1] * nums[i], g[i - 1] * nums[i]))
            
                # 看看是當前這個數比較小，還是前面的最大乘積或最小乘積乘以當前的數後比較小
                g[i] = min(g[i], min(f[i - 1] * nums[i], g[i - 1] * nums[i]))

        # print(f)
        # print(g)

        return max(f)
