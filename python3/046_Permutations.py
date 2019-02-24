class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 空 (null) 和空的 list 是不同的
        # null 就是什麼都沒有
        # 空的 list 是有一個 list，只是 list 裡面是空的
        if nums is None: # nums 是指向空 Null
            return []
        if nums is []: # nums 是一個空的 list
            return [[]]
        
        results = []
        permutation = []
        hash_set = dict()
        # self.dfs(nums, results, permutation) # 簡單的方式
        self.dfs(nums, results, permutation, hash_set) # 用哈希表
        return results

    # 簡單的方式:
#     def dfs(self, nums, results, permutation):
#         if len(permutation) == len(nums):
#             results.append(permutation[:])
#             return results
            
#         for i in range(len(nums)):
#             if nums[i] in permutation:
#                 continue
#             permutation.append(nums[i])
#             self.dfs(nums, results, permutation)
#             permutation.pop()

    # 用哈希表
    def dfs(self, nums, results, permutation, hash_set):
        if len(permutation) == len(nums):
            results.append(permutation[:])
            return results
        
        for i in range(len(nums)):
            if nums[i] in hash_set: # nums[i] 是 key 這邊就是 if key in dict
                continue
            permutation.append(nums[i])
            hash_set[nums[i]] = 1
            self.dfs(nums, results, permutation, hash_set)
            del hash_set[nums[i]]
            permutation.pop()
