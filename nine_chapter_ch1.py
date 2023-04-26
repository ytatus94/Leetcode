class Solution:
    # 13 Implement strStr()
    def str_str(self, source: str, target: str) -> int:
        if source is None or target is None:
            return 0

        if target not in source:
            return -1
        else:
            return source.index(target)

    # 17 Subsets
    def subset(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []

        nums = sorted(nums)

        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, curr_index, curr_subset, result):
        if curr_index == len(nums):
            result.append(curr_subset.copy()) # 深拷貝
            return

        self.dfs(nums, curr_index + 1, curr_subset + [nums[curr_index]], result)
        self.dfs(nums, curr_index + 1, curr_subset, result)

    def dfs(self, nums, curr_index, curr_subset, result):
        result.append(curr_subset.copy()) # 深拷貝

        for i in range(curr_index, len(nums)):
            curr_subset.append(nums[i])
            self.dfs(nums, i + 1, curr_subset, result)
            curr_subset.pop()

    # 18. Subsets II
    def subset_with_dup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []

        nums = sorted(nums)

        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, curr_index, subset, result):
        result.append(subset.copy())
        for i in range(curr_index, len(nums)):
            if i > curr_index and nums[i] == nums[i - 1]: # 去重
                continue
            self.dfs(nums, i + 1, subset + [nums[i]], result)
