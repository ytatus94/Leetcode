class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        result = [-1, -1]
        if len(A) == 0:
            return result

        result[0] = self.find_first_position(A, target)
        result[1] = self.find_last_position(A, target)
        
        return result
        
    def find_first_position(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
    def find_last_position(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] <= target:
                start = mid
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
