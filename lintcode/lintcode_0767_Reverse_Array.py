# 方法1:
class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        nums.reverse()

# 方法2:
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
