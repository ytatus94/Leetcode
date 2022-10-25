from typing import (
    List,
)

class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverse_array(self, nums: List[int]):
        # write your code here
        # 注意要 inplace
        i = 0
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
