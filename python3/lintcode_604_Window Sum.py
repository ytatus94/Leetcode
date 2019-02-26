# lintcode 604
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums is None or len(nums) < k or k <= 0:
            return []
        
        # 同向雙指針：頭指向 i 尾指向 i+k-1
        res = []
        # 先計算從 0 開始的前 k 個元素的和
        sum = 0
        for i in range(k):
            sum += nums[i]
        res.append(sum)
        
        for i in range(1, len(nums) - (k-1)):
            sum = sum - nums[i - 1] + nums[i+k-1]
            res.append(sum)
            
        return res
        # 超時
        # for i in range(len(nums) - (k-1)):
        #     subarray = nums[i: i+k]
        #     res.append(sum(subarray))
        # return res
