class Solution:
    def twoSum(self, nums, target):
        if nums is None or len(nums) < 2:
            return 0
            
        nums = sorted(nums)
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
                
        return count
