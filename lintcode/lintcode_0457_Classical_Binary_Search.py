class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 # 記得用整數除法
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
