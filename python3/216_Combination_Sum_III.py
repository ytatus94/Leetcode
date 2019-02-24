class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        # 要從 1 ~ 9 的數組裡面選 k 個出來，不可重複，和等於 n
        # 所以先建立一個 1 ~ 9 的數組，然後跑 DFS
        nums = [i for i in range(1, 10)]
        results = []
        self.dfs(nums, k, n, 0, results, [])
        return results
    
    def dfs(self, nums, numCounts, target, index, results, curr):
        # 要滿足 k (numCounts) 個元素的和為 n (target)
        if sum(curr) == target and len(curr) == numCounts:
            results.append(curr[:])
            return
        for i in range(index, len(nums)):
            if sum(curr + [nums[i]]) > target:
                break
            # 不可以重複選取，所以要從 i + 1 開始
            self.dfs(nums, numCounts, target, i+1, results, curr + [nums[i]])
