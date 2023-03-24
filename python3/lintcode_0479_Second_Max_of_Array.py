class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        return sorted(nums)[-2]

# 打擂台
from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def second_max(self, nums: List[int]) -> int:
        # write your code here        
        max_1st = max(nums[0], nums[1])
        max_2nd = min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > max_1st:
                max_2nd = max_1st
                max_1st = nums[i]
            elif nums[i] > max_2nd:
                max_2nd = nums[i]
        print(max_1st, max_2nd)
        return max_2nd

