from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        # 假設 left 的左邊都是排好的 0
        #     right 的右邊都是排好的 2
        left = 0
        right = len(nums) - 1
        i = 0
        # 遇到 0 就往左邊丟
        # 遇到 1 就把 i 往右移動一格
        # 遇到 2 就往右邊丟
        while i <= right: # 注意要有等號
            if nums[i] == 0:
                # 當遇到 0 的時候就和 nums[left] 互換，然後再把 left 加ㄧ
                # 這樣確保 left 左邊都是 0
                nums[i], nums[left] = nums[left], nums[i] 
                left += 1
                i += 1
            elif nums[i] == 2:
                # 當遇到 2 的時候就和 nums[right] 互換，然後再把 right 減ㄧ
                # 這樣確保 right 右邊都是 2
                # i 不往右邊移，因為此時 nums[i] 還要和 0 比較
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
