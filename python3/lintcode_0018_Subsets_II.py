from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if nums is None:
            return []

        nums = sorted(nums)
        result = []
        current = []
        self.dfs(nums, 0, current, result)
        return result

    # 定義: 傳回所有以 current 開頭的子集
    def dfs(self, nums, start_index, current, result):
        result.append(current.copy()) # 要深度拷貝
        # 拆解:
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.dfs(nums, i + 1, current, result)
            current.pop()
        
