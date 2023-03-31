class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 開兩個數組紀錄以第 i 個元素結尾的 subarray 最大和最小乘積
        dp_max = [None] * len(nums)
        dp_min = [None] * len(nums)
        # 初始條件: 第一個元素的乘積就是自己
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        # subarray 的最大乘積可能是元素 i 自己，也可能是 nums[i] 之前的最大乘積再乘上 nums[i]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))
            dp_min[i] = min(nums[i], min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))

        return max(dp_max)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = nums[:]
        prod_inv = nums[::-1] # 不懂為什麼要取反向的乘積
        for i in range(1, len(nums)):
            prod[i] *= prod[i - 1] or 1 # 用 1 是避免出現 nums[i]=0 的情況
            prod_inv[i] *= prod_inv[i - 1] or 1
        return max(prod + prod_inv) # 不懂
