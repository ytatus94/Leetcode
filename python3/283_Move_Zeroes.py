class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
            
# lintcode 539
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        i = 0 # 用來回圈每個元素
        j = 0 # 指向 0 的元素
        while i < len(nums):
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            if nums[j] != 0:
                j += 1
            i += 1
