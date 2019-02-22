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

# lintcode 63
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return False
        return target in A
