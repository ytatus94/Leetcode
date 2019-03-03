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

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            # 把 j 移到下一個 0 所在位置
            # 注意 j 要小於 i 不然會出錯
            # 例如 [5,4,3,2,1] 中都沒有 0 所以當 i = 0 時，j 會移動到 j=5 就超出了 len(nums) 的長度
            while j < i and nums[j] != 0:
                j += 1
            i += 1
