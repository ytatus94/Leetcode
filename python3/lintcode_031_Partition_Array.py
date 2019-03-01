# lintcode 031
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] >= k:
                return i
        return len(nums)

class Solution:
    def partitionArray(self, nums, k):
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            # 當 start 和 end 所代表的元素滿足 < k 和 >= k 的要求時
            # 只是往下/往前移動一個
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
