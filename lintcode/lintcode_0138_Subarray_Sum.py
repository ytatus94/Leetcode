# lintcode 138
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # [m, n] 的數組和為 0 ==> 前綴和 presum[m-1] = presum[n]
        
        prefix_hash = {0: -1} # key 是 prefix_sum，val 是 index
        prefix_sum = 0
        
        for idx, val in enumerate(nums):
            prefix_sum += val
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, idx
            prefix_hash[prefix_sum] = idx
            
        return -1, -1
