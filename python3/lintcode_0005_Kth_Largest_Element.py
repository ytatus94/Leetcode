from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        # write your code here
        nums = sorted(nums)
        if k <= len(nums):
            return nums[-k]
        else:
            return -1
