class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 規定要用 O(logn)，所以一定是二分法
        # 可以用兩個二分法
        # 第一個二分法先找到數列中最小值 (Find minimum in rotated sorted array)
        # 然後判斷 target 是在上半段 (比第一個元素大) 還是下半段 (比第一個元素小)
        # 然後用普通的二分法來找 target
        
        # 也可以只用一個二分法來找，要考慮的情況就變成
        # M 在上半段時
        # 1.) S ... T ... M ... 最小值 ... E
        # 2.) S ... M ... T ... 最小值 ... E
        # 3.) S ... M ... 最小值 ... T ... E
        # M 在下半段時
        # 4.) S ... T ... 最小值 ... M ... E
        # 5.) S ... 最小值 ... T ... M ... E
        # 6.) S ... 最小值 ... M ... T ... E
        # M 是在上半段還是下半段就和 nums[0] 比較

        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[0]: # 1, 2, 3 的情形
                if nums[mid] >= target and target >= nums[start]: # 1
                    end = mid
                else: # 2, 3
                    start = mid
            else: # 4, 5, 6 的情形
                if nums[mid] <= target and target <= nums[end]: # 6
                    start = mid
                else: # 4, 5
                    end = mid
        # 最後剩下 start 和 end 要和 target 比較
        # 但是 target 也有可能不存在
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
