class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 第一棟和最後一棟房子相連，所以不能同時偷
        # 要拆開成兩種情況討論，變成兩個普通的 house robber I 問題
        res1 = self.house_robber(nums[:-1]) # 不偷第一棟房子
        res2 = self.house_robber(nums[1:]) # 不偷最後一棟房子
        return max(res1, res2)

    # 一般的方式
    # def house_robber(self, nums):
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]

    #     dp = [0 for i in range(len(nums) + 1)]
    #     dp[0] = 0
    #     dp[1] = nums[0]

    #     for i in range(2, len(nums) + 1):
    #         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    #     return dp[len(nums)]

    # 用滾動數組的方式
    def house_robber(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        old = 0
        new = nums[0]

        for i in range(2, len(nums) + 1):
            t = max(new, old + nums[i - 1])
            old = new
            new = t
        return new
