class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        
        left = 0
        right = len(nums) - 1
        i = 0
        
        while i <= right:
            # 如果 i 遇到的是 0 就往左邊丟
            # 如果 i 遇到的是 1 就 i 變 i + 1
            # 如果 i 遇到的是 2 就往右邊丟
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
                
# lintcode 148
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        
        left = 0
        right = len(nums) - 1
        i = 0
        
        # 左右兩陣營
        # 左邊陣營是 0 右邊陣營是 2
        while i <= right:
            if nums[i] == 0: # 等於 0 時往左邊丟
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 1: # 等於 1 時什麼都不幹，直接往下移動一格
                i += 1
            else: # 等於 2 的時候往右邊丟
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # 因為原本的 nums[right] 不知道是 0, 1, 2 哪一個
                # 所以交換後還需要再判斷，才能知道可不可以 i++
                # 因此這邊不會對 i 移動到下一格
