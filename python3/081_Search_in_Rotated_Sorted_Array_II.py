class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        # 有重複的 rotated sorted array 只能用 for 循環
        # for i in nums:
        #     if i == target:
        #         return True
        # return False
        
        # 更簡單的方法，又跑得快
        return target in nums
