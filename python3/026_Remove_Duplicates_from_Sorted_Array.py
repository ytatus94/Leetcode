class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用雙指標 i 負責更改原本的 array，j 負責讀取原本的 array
        i = j = 0
        while j < len(nums):
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                j = j + 1
            # 離開迴圈時 j 是停在最後一個重複的元素上
            nums[i] = nums[j]
            i += 1
            j += 1
        # 離開迴圈時 i 正好等於新的 array 的長度
        
        return i
        
class Solution:    
    # 基本上和 443. String Compression 一樣
    def removeDuplicates(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        
        # 已經排序過就不需要再排序
        # nums = sorted(nums)
        
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
            
        return index + 1
