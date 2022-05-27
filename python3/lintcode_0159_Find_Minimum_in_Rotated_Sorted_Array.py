from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        min_val = float("inf")
        for i in nums:
            if i < min_val:
                min_val = i
        return min_val

    from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        target = nums[-1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] < target:
                end = mid
            else:
                start = mid

        print("out:", start, end)
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
