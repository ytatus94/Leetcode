class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 使用 DFS 和 BFS 都可以
        # 題目有 "all" possible 第一個要想到 DFS
        # DFS 就是用來解決"找出滿足某條件的所有方案"的算法
        # DFS 是用遞迴的方法來實現


        if not nums:
            return []
        
        nums.sort() # 要先排序
        results = []
        subset = []
        self.helper(nums, results, subset, 0)
        return results   
    
    # 方法一
    # 和 C++ 的一樣，但是跑了 84ms 只 beat 2%
    # def helper(self, nums, results, subset, current_index):
    #     results.append(subset.copy()) # 注意要用 deep copy
    #     for i in range(current_index, len(nums)):
    #         subset.append(nums[i])
    #         self.helper(nums, results, subset, i + 1)
    #         subset.pop()
        

    # 方法二
    def helper(self, nums, results, subset, current_index):
        if current_index == len(nums): # 跑到底了，可以塞給 result
            results.append(subset[:]) # 注意 subset 要用 deep copy
            return results
        self.helper(nums, results, subset + [nums[current_index]], current_index + 1)
        self.helper(nums, results, subset, current_index + 1) # 會跑到這行時，表示上一行已經跑到底，又一直 return 到 current_index 所指向的元素，所以 current_index 可以往後移動一個元素了
        
# lintcode 17
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None:
            return []
            
        nums = sorted(nums)
        results  = []
        subset = []
        self.dfs(nums, results, subset, 0)
        
        return results
        
    # def dfs(self, nums, results, subset, index):
    #     if index == len(nums):
    #         results.append(subset[:])
    #         return results
            
    #     self.dfs(nums, results, subset + [nums[index]], index + 1)
    #     self.dfs(nums, results, subset, index + 1)
    
    def dfs(self, nums, results, subset, index):
        results.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[index])
            self.dfs(nums, results, subset, index + 1)
            subset.pop()
