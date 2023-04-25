from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        prefix_sum = 0
        max_sum = -sys.maxsize
        min_sum = 0

        for i in nums:
            prefix_sum += i
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
