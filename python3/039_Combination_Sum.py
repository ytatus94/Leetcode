class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. 去重 + 排序
        nums = sorted(list(set(candidates)))
        
        # 2. 遞歸函數進行 DFS
        results = []
        combination = []
        self.dfs(nums, 0, results, combination, 0, target)
        return results
    
    # Traversal
    # 遞歸的定義: 尋找所有以 combination 開頭的組合，放到 results
    def dfs(self, nums, start_index, results, combination, sum, target):
        # 遞歸的出口:
        if sum == target:
            copy = combination[:]
            results.append(copy) # deep copy
            return
        
        # 遞歸的拆解:
        for i in range(start_index, len(nums)):
            if sum + nums[i] > target:
                break
            combination.append(nums[i])
            # 因為可以重複選取，所以 start_index 仍然是從 i 開始
            self.dfs(nums, i, results, combination, sum + nums[i], target)
            combination.pop()

# lintcode 135
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates is None:
            return []
            
        nums = sorted(list(set(candidates)))
        
        results = []
        self.dfs(nums, target, 0, results, [])
        return results
        
    def dfs(self, nums, target, index, results, curr):
        if sum(curr) == target:
            results.append(curr.copy())
            return
        
        for i in range(index, len(nums)):
            if sum(curr + [nums[i]]) > target:
                break
            # 由於可以重複選取，所以 index 仍然從 i 開始
            self.dfs(nums, target, i, results, curr + [nums[i]])
