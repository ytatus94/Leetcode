from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
             we will sort your return value in output
    """
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        nums = sorted(nums)

        # 要標記有沒有使用過
        visited = [0 for i in range(len(nums))]

        result = []
        self.dfs(nums, 0, [], result, visited)
        return result

    def dfs(self, nums, start_index, curr_subset, result, visited):
        # 當 curr_index 和 nums 長度一樣的時候，就是每個數都用過了
        # 可以塞到 result 裡面去
        if len(curr_subset) == len(nums):
            result.append(curr_subset.copy()) # 深拷貝

        for i in range(len(nums)):
            # 用過了就不能再用
            if visited[i] == 1:
                continue

            # 如果和前一個數重複，而且前一個數還沒用過，那這個數就不能用
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue

            visited[i] = 1 # 標記成用過了再傳入 dfs
            self.dfs(nums, i + 1, curr_subset + [nums[i]], result, visited)

            visited[i] = 0 # 回朔
