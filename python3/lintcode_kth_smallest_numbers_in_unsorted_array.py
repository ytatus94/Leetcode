class Solution:
    def kthSmallest(k, nums):
        return self.quick_select(nums, 0, len(nums) - 1, k - 1)
        
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
            
        left = start
        right = end
        
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
            if right >= k and start <= right:
                return self.quick_select(nums, start, right, k)
            elif left <= k and left <= end:
                return self.quick_select(nums, left, end, k)
                
            未完...
