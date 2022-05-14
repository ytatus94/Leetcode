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

    # 方法一是每次 subset 有新的數加入之後，就塞到 results 裏面
    # 所以方法一的結果是 [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3],[3]]
    # 方法二是跑到底了，才把整個 subset 加入到 results 裏面
    # 所以方法二的結果是 [[1,2,3], [1,2], [1,3], [1], [2,3], [2],[3], []]
    # 兩者放入 results 的順序不一樣

    # 方法二
    def helper(self, nums, results, subset, current_index):
        if current_index == len(nums): # 跑到底了，可以塞給 result
            results.append(subset[:]) # 注意 subset 要用 deep copy
            return results
        self.helper(nums, results, subset + [nums[current_index]], current_index + 1) # 要把 nums[current_index] 放入 subset 中
        self.helper(nums, results, subset, current_index + 1) # 不把 nums[current_index] 放入 subset 中，會跑到這行時，表示上一行已經跑到底，
                                                              # 又一直 return 到 current_index 所指向的元素，所以 current_index 可以往後移動一個元素了

# 方法三
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return []
        
        results = [] # results 宣告放到 if 後面會比較快
        dfs(results, [], nums)

        return results
    
def dfs(results, subset, rest):
    results.append(subset)
    for i in range(len(rest)):
        dfs(results, subset + [rest[i]], rest[i+1:])
# 當 rest[i] 已經是列表中最後一個數的時候，rest[i+1:] 理論上是超過了會傳回錯誤才對，但是實際上 python 會傳回一個空列表 []
# 所以變成 dfs(results, subset + [最後一個數], [])
# 而 len([]) = 0 --> range(len(rest)) = range(0, 0) 因此不會進入 for loop
# 只有第一行的 results.append(subset) 被執行

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
