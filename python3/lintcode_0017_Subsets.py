from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if nums is None:
            return []
        
        result = []
        nums = sorted(nums)
        self.dfs(nums, 0, [], result)
        return result

    # 定義: 傳回以 current 開頭的所有子集
    def dfs(self, nums, start_index, current, result):
        # 出口:
        if start_index == len(nums):
            result.append(current.copy()) # 要深度拷貝
            return
        # 拆解
        current.append(nums[start_index]) # 要放入 nums[start_index]
        self.dfs(nums, start_index + 1, current, result)

        current.pop() # 不要放入 nums[start_index]
        self.dfs(nums, start_index + 1, current, result)

