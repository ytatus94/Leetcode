# lintcode 058
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        if numbers is None or len(numbers) < 4:
            return []
            
        nums = sorted(numbers)
        
        results = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i+1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        results.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                        start += 1
                    else:
                        end -= 1
                        
        return results
