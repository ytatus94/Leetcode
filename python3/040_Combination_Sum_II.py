class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        combination = []
        # 現在 candidates 中有重複的數字
        # 但是在從 candidates 選的時候，同一個數不可以重複選取
        # 相同數值，但是在不同的 index 的數字，是要當成兩個不同的數
        nums = sorted(list(candidates)) # 排序，不去重
        self.dfs(nums, 0, results, combination, 0, target)
        return results
    
    def dfs(self, nums, start_index, results, combination, sum, target):
        if sum == target:
            results.append(combination[:]) # 注意要用 deep copy
            return
        
        for i in range(start_index, len(nums)):
            # 要比對是否和前一個數字的數值相同
            # 如果相同，有可能會選出一樣的組合，造成數字重複選取，所以不可以
            # 例如: [1(1), 2, 5], [1(2), 2, 5] 第一個 1 和第二個 1 都選了 2, 5
            # 這樣子就是 2, 5 重複選取了
            if i != start_index and nums[i] == nums[i - 1]:
                continue
            if sum + nums[i] > target:
                break
            combination.append(nums[i])
            # 下一個要從第 i + 1 個數開始選起，因為不可重複選取同一個數字
            self.dfs(nums, i + 1, results, combination, sum + nums[i], target)
            combination.pop()
