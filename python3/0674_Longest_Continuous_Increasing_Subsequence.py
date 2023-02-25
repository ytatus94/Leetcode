class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        max_length = 0
        curr_length = 1 # 一開始在第一個數，長度是 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_length += 1
            else:
                curr_length = 1
            if curr_length > max_length:
                max_length = curr_length
        return max_length
