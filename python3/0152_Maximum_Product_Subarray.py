class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 開兩個數組紀錄以第 i 個元素結尾的 subarray 最大和最小乘積
        dp_max = [None] * len(nums)
        dp_min = [None] * len(nums)
        # 初始條件: 第一個元素的乘積就是自己
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))
            dp_min[i] = min(nums[i], min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))

        return max(dp_max)
