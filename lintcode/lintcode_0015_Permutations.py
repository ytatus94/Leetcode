from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        nums = sorted(nums)

        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start_index, curr_subset, result):
        # 如果 curr_subset 和 nums 長度相等，表示所有的數都用了
        # 所以可以塞到 result 裡面
        if len(curr_subset) == len(nums):
            result.append(curr_subset.copy())
            return

        for i in range(len(nums)): # 因為每個數都要用，所以要從頭開始循環
            if nums[i] in curr_subset: # 已經用過的數就跳過
                continue
            self.dfs(nums, i + 1, curr_subset + [nums[i]], result)
