class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums) // 2
        # 要讓 min(ai, bi) 的和最大
        # 最好的方式就是讓 nums 排序，然後兩兩一組
        # 才會有小的與小的一組，大的與大的一組
        # 這樣 min(i, i+1) = i
        # min(ai, bi) 的和就會是所有第基數個元素的和
        # 因為 index 是從 0 開始，所以第基數個元素就是 index % 2 == 0 的
        # sorted_nums = sorted(nums)
        # sum  = 0
        # for i, val in enumerate(sorted_nums):
        #     if i % 2 == 0:
        #         sum += val
        
        min_values = [val for i, val in enumerate(sorted(nums)) if i % 2 == 0]
        return sum(min_values)
