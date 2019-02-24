class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if nums is []:
            return [[]]
        
        results = []
        permutation = []
        nums = sorted(nums) # 要先排序
        # 因為 nums 中有重複的數值，所以要記錄一下該數值是否用過了
        visited = [0 for i in range(len(nums))] # 用來標記第 i 個元素是否訪問過了
        self.dfs(nums, results, permutation, visited)
        return results
    
    def dfs(self, nums, results, permutation, visited):
        if len(permutation) == len(nums):
            results.append(permutation[:])
            return results
        
        for i in range(len(nums)):
            if visited[i] == 1: # 用過了不可以再用
                continue
                
            # 若現在這個元素，和前面那個元素的數值相同，
            # 但是前面那個還沒有用過，就不可以使用現在這個
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue
                
            permutation.append(nums[i])
            visited[i] = 1 # 用過就標記 1
            self.dfs(nums, results, permutation, visited)
            visited[i] = 0 # 沒用過就標記 0
            permutation.pop()
