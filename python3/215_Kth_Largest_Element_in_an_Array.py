class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        # 如果有四個數，找第一大，就相當於找第四小
        # 找第二大，就相當於找第三小
        # 找第三大，就相當於找第二小
        # 找第四大，就相當於找第一小
        # 所以找第 n 大，就相當於找第 m 小，然後 n + m = size + 1
        # ==> 題目要找第 k 大，相當於找第 len - k + 1 小
        # 但是第幾大或第幾小是從 1 開始計算，程式的 index 是從 0 開始算
        # 要再減 1 ==> len - k + 1 - 1 = len - k
        return self.findKthSmallest(nums, 0, len(nums) - 1, len(nums) - k)
    
    def findKthSmallest(self, nums, start, end, k):
        if start == end:
            return nums[k]
        
        left = start
        right = end
        pivot = nums[(start + end)//2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if start <= k and k <= right:
            return self.findKthSmallest(nums, start, right, k)
        elif left <= k and k <= end:
            return self.findKthSmallest(nums, left, end, k)
        else:
            return nums[k]
            
# lintcode 005
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
            
        # n 超過範圍了的時候
        if n < 1 or n > len(nums):
            return -1
            
        # quick select 是用來找第 k 小的元素
        # 要找第 k 大的元素，相當於找第 len-k 小的元素
        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)
        
    def partition(self, nums, start, end, k):
        if start >= end:
            return nums[k]
            
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
                
        if right >= k:
            return self.partition(nums, start, right, k)
        if left <= k:
            return self.partition(nums, left, end, k)
        
        return nums[k]
