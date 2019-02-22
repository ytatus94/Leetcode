class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 一樣用 DFS 但是要去除重覆的
        # 因為 [1, 2_1, 2_2] 和 [1, 2_2, 2_1] 都是 [1, 2, 2] 只能留一個
        # 這種題目都先排序一下
        
        if not nums:
            return []
        
        results = []
        nums.sort()
        self.dfs(nums, results, [], 0)
        return results
    
    def dfs(self, nums, results, subset, index):
        results.append(subset[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]: # 這邊在去重
                continue
            self.dfs(nums, results, subset + [nums[i]], i + 1)
