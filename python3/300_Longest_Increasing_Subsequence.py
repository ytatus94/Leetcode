# lintcode 076
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        # status and initialize
        # 所有的點都可能是起點，每個元素自己的長度是 1
        f = [1 for i in range(len(nums))]
        # function
        # 從 i 前面的某個元素 j 跳到 i 上面
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 上升序列
                    f[i] = max(f[i], f[j] + 1)
        # 所有的值都可能是終點
        # 所以要去找一個最大的 f[i]
        max_LIS = 0
        for i in range(len(nums)):
            max_LIS = max(max_LIS, f[i])
            
        return max_LIS
