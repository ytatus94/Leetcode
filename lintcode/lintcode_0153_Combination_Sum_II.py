from typing import (
    List,
)

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
             we will sort your return value in output
    """
    def combination_sum2(self, num: List[int], target: int) -> List[List[int]]:
        # write your code here
        # 每個數只能選一次，但是 num 中有重複的數值
        # 所以只把 num 排序就好 (不去重)
        nums = sorted(num)

        result = []
        self.dfs(nums, 0, [], result, target)
        return result

    def dfs(self, nums, start_index, curr_subset, result, target):
        # 如果 curr_subset 的和與 target 一樣，就放到 result 裡面
        if sum(curr_subset) == target:
            result.append(curr_subset.copy()) # 要用深拷貝

        for i in range(start_index , len(nums)):
            # 要避免重複的數值 (因為排序過了，所以是避免和前一個數重複)，還有不可以超出 target
            if i != start_index and nums[i] == nums[i - 1]:
                continue
            if sum(curr_subset) + nums[i] > target:
                break
            self.dfs(nums, i + 1, curr_subset + [nums[i]], result, target)
