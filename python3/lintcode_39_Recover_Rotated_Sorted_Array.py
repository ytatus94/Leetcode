# lintcode 39
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return
        
        # for i in range(len(nums)):
        #     if nums[i] > nums[i + 1]:
        #         nums = nums[i+1:] + nums[:i+1] # 這樣子輸出雖然正確，但是不是 in-place
        #         print(nums)
        #         break
        
        # 三步翻轉法
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                self.swap(nums, 0, i+1)
                self.swap(nums, i+1, len(nums))
                self.swap(nums, 0, len(nums))
                break
          
    def swap(self, nums, start, end):  
        temp = nums[start:end]
        temp = temp[::-1]
        for i in range(len(temp)):
            nums[start + i] = temp[i]
