# lintcode 061
# 方法 1:
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

# 方法 2:
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        # write your code here
        if a is None or len(a) == 0:
            return [-1, -1]

        first = self.find_first_position(a, target)
        last = self.find_last_position(a, target)
        return [first, last]

    def find_first_position(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] >= target:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

    def find_last_position(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1
