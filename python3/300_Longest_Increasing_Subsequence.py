# 方法1: 暴力法 O(N^2)
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

# 方法2: 用二分法 O(NlogN) 比較快
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        # 建立用來保存 LIS 的 list
        # 用 binary search, dp 只會有正確的長度，不一定會有正確的 LIS 結果
        # 這是因為把許多可能的 LIS 都不斷地重複寫在同一個 dp 的記憶體上面 
        dp = []

        # 先把第一個數放入
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i]) # 如果 nums[i] 比目前 LIS 中最後一個還大，就加入 LIS 中
            else:
                # 找出 dp[j - 1] < nums[i] < dp[j] 的部分，然後把 dp[j] 用 nums[i] 取代 
                insert_index = self.binary_search(dp, nums[i])
                dp[insert_index] = nums[i]
        
        return len(dp)
    
    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # target 在後半段，所以把 start 移到 mid
                start = mid
            elif nums[mid] > target: # target 在前半段，所以把 end 移到 mid
                end = mid

        if nums[start] < target:
            return start + 1
        elif nums[start] >= target:
            return start
        

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
