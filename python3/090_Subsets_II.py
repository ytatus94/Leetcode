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
            # 傳入 subset + [num[i]] 這樣就不用處理在 DFS 之前先在 subset 中加入一個，然後還要在 DFS 之後在 subset 中回朔的問題

# 方法2:
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        
        results = []
        # nums 有重複的值，所以要先排序
        # sorted(list) 會傳回新的 list
        # list.sort() 則是 inplace
        sorted_nums = sorted(nums)
        dfs(results, [], sorted_nums)
        return results
    
def dfs(results, subset, rest):
    results.append(subset)
    for i in range(len(rest)):
        # 如果目前循環到的數 rest[i] 和前一個數 rest[i-1] 一樣
        # 那就跳過目前的循環，才不會產生重複的 subset
        # 但是當 i = 0 時，i -1 = -1 會變成取出 rest[-1]
        # 這反而不對了，所以要避開 i = 0 的狀況
        if i != 0 and rest[i] == rest[i - 1]:
            continue
        dfs(results, subset + [rest[i]], rest[i+1:])
