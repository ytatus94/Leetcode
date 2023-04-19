from typing import (
    List,
)

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        # 每一個數可以重複選取
        # 要先去重，然後排序
        nums = sorted(list(set(candidates)))

        result = []
        self.dfs(nums, 0, [], result, target)
        return result

    def dfs(self, nums, start_index, curr_subset, result, target):
        # 出口
        if sum(curr_subset) == target:
            # 如果當前 subset 的和與 target 相同，就放到 result 裡面
            result.append(curr_subset.copy()) # 要用深拷貝
            return

        for i in range(start_index, len(nums)):
            # 先看有沒有超出 target
            # 因為 nums 是排序過的，如果加上 nums[i] 那加上 nums[j > i] 也一定超出 target 
            if sum(curr_subset) + nums[i] > target:
                break
            # 因為每個數可以重複選取，所以依然從 i 開始
            self.dfs(nums, i, curr_subset + [nums[i]], result, target)


