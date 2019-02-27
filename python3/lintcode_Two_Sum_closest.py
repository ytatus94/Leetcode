class Solution:
    def twoSumClosest(nums, target):
        if nums is None:
            return -1
            
        nums = sorted(nums)
        
        left = 0
        right = len(nums) - 1
        best = sys.maxsize
        
        while left < right:
            diff = abs(nums[left] + nums[right] - target)
            best = min(best, diff)
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
                
        return best
