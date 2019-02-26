class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0 # 前 i 個數的和
        max_sum = -sys.maxsize # 一開始給一個很小的值
        min_sum = 0 # 前 i 個數 0 ~ k 個數的和的最小值
        
        for n in nums:
            prefix_sum += n
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            
        return max_sum
        
# lintcode 44
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None:
            return None
        
        sum = 0
        max_sum = -sys.maxsize
        min_sum = 0
        
        for i in nums:
            sum += i
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(min_sum, sum)
            
        return max_sum
