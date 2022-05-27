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
