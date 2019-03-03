class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None or len(nums) < 4:
            return []
        
        nums = sorted(nums) # 要記得先排序
        
        res = []
        # 固定 i, j 看 j 之後的數組成的 two sum
        # 所以 i 的最後一個元素後面必須還有 3 個元素，因此用 len(nums) - 2
        # 同理 j 的最後一個元素後面必須還有 2 個元素，因此用 len(nums) - 1
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: # i 去重
                continue
                
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]: # j 去重
                    continue
                
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # 要記得還要再去重，把 start 和 end 移動到不同的數
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif sum < target:
                        start += 1
                    else:
                        end -= 1
                        
        return res
        
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
