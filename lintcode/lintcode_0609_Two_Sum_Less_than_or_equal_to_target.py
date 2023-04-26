class Solution:
    def twoSum2(self, nums, target):
        if nums is None or len(nums) < 2:
            return None
            
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1
                
        return count
