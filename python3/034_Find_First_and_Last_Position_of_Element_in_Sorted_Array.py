class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        first = self.findFirstPosition(nums, target)
        last = self.findLastPosition(nums, target)
        return [first, last]
        
    def findFirstPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
    
    def findLastPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
