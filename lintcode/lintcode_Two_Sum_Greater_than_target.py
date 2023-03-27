class Solution:
    def twoSum2(self, nums, target):
        if nums is None or len(nums) < 2:
            return None
            
        nums = sorted(nums)
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                count = right - left
                right -= 1
                
        return count
