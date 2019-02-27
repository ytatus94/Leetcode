class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            sum = numbers[start] + numbers[end]
            
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else: # sum == target 等於表示找到了
                pairs = []
                pairs.append(start + 1) # 題目說 index 是 not zero-based
                pairs.append(end + 1)
                
                return pairs
            
        return None
        
# lintcode 608
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        head = 0
        tail = len(nums) - 1
        while head < tail:
            if nums[head] + nums[tail] > target:
                tail -= 1
            elif nums[head] + nums[tail] < target:
                head += 1
            else:
                return [head+1, tail+1] # 要回傳 non-zero based 的 index
        return None
