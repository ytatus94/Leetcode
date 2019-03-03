class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []
        
        nums = sorted(nums)
        
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            start = i + 1
            end = len(nums) - 1
            target = -1 * nums[i]
            
            while start < end:
                if nums[start] + nums[end] == target:
                    res.append([-1 * target, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
                    
        return res
    
# lintcode 057
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) < 3:
            return None
            
        res = []
        head = 0
        tail = 2
        nums = sorted(numbers)
        
        for i in range(0, len(nums) - 2):
            # 重複的數要刪除掉
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            subarray = nums[:i]
            target = -1 * nums[i]
            start = i + 1
            end = len(nums) - 1
            res += self.two_sum(nums, target, start, end)
            
        return res
        
    def two_sum(self, nums, target, start, end):
        result = []
        while start < end:
            if nums[start] + nums[end] == target:
                result.append([-1 * target, nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return result
