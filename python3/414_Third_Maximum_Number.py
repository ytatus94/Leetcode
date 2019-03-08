class Solution:
    def thirdMax(self, nums: 'List[int]') -> 'int':
        nums = list(set(nums)) # 去重
        
        if len(nums) < 3:
            return max(nums)
        
        first, second, third = float('-Inf'), float('-Inf'), float('-Inf')
        
        for num in nums:
            if num > first: # 原先的第一第二名往後挪
                first, second, third = num, first, second
            elif num > second: # 第二名往後挪
                second, third = num, second
            elif num > third:
                third = num
        return third
