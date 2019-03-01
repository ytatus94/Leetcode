# lintcode 059
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if numbers is None or len(numbers) < 3:
            return -1
            
        nums = sorted(numbers)
        
        best_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) -2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if abs(target - sum) < abs(target - best_sum):
                    best_sum = sum
                if sum < target:
                    start += 1
                else:
                    end -= 1
        return best_sum
