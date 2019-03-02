class Solution:
    def kthSmallest(self, k, nums):
        return self.quick_select(nums, 0, len(nums) - 1, k - 1) # 從 0 開始，第 k 小的數是第 k - 1
        
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
            
        left = start
        right = end
        
        pivot = nums[(start + end) // 2]
        
        # 這個部分就是 quick sort
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            # 離開迴圈時 left 停在比 pivot 大的元素上
            while left <= right and nums[right] > pivot:
                right -= 1
            # 離開迴圈時 right 停在比 pivot 小的元素上
            
            # 所以要交換 left 和 right 的元素
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 離開迴圈時 right 會比 left 小，變成 start ... right left ... end 的順序
        
        # 要找第 k 小，如果 right 比 k 還大，那一定是在 start ... right 這段
        # 如果 k 比 left 還大，那一定是在 left ... end 這段
        if right >= k and start <= right:
            return self.quick_select(nums, start, right, k)
        elif left <= k and left <= end:
            return self.quick_select(nums, left, end, k)
        else: # 一直切分下去，最後一定會剩下一個剛好就是第 k 個的
            return nums[k]
