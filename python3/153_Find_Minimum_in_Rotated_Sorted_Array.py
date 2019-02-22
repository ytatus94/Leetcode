class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 其實就是找第一個比 target 小的數
        # 但是題目沒給 target
        # 要知道 target 其實是 nums 的最後一個數
        start = 0
        end = len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = target
            elif nums[mid] > target: # mid 在上半部
                start = mid
            elif nums[mid] < target: # mid 在下半部
                end = mid
        if nums[start] <= target:
            return nums[start]
        else:
            return nums[end]
