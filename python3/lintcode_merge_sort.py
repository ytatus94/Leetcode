class Solution:
    def sortIntegers2(self, nums):
        temp = [None] * len(nums)
        mergeSort(nums, 0, len(nums) - 1, temp)
    
    def mergeSort(self, nums, start, end, temp):
        if start >= end:
            return
            
        left = start
        right = end
        mid = (left + right) // 2
        
        mergeSort(nums, start, mid, temp)
        mergeSort(nums, mid + 1, end, temp)
        merge(nums, start, mid, end, temp)
        
    def merge(self, nums, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start
        
        # merge two sorted subarray of nums to result array
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                index += 1
                left += 1
            else:
                temp[index] = nums[right]
                index += 1
                right += 1
        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1
        
        # copy temp back to nums
        for index in range(start, end+1):
            nums[index] = temp[index]
