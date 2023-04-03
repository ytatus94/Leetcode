class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        dp = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            dp[i] = 1 # 自己就是一個子序列
            for j in range(i): # 數字不需要相鄰，只要前面有比自己小的，就列入計算
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)

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
