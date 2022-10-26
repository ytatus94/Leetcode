# 方法1: 很慢
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            if i in hash_map.keys():
                return True # 已經在 hash map 中了，就表示有重複，可以直接不看其他的數了
            else:
                hash_map[i] = 1
        return False
      
# 方法2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not(len(nums) == len(set(nums))) # 如果長度一樣表示沒有重複的數字，這時候要回傳 False 所以需要一個 not 在前面
