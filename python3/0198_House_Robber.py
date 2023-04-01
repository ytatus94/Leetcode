class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # 只有一棟房子，那就偷該棟房子
        if len(nums) == 1:
            return nums[0]

        dp = [0 for i in range(len(nums) + 1)]

        dp[0] = 0 # 偷前 0 棟房子得到 0 元
        dp[1] = nums[0] # 偷前一棟房子，那可偷可不偷，所能偷到最大的金額當然就是要偷
        dp[2] = max(nums[0], nums[1]) # 偷前兩棟房子，但是只能選一棟偷，所以選最大的偷

        # 偷前 i 棟房子，最後一棟編號是 i-1
        # 1.) f[i][偷編號 i-1 的房子] = f[i-1][不能偷編號 i-2 的房子] + nums[i-1]
        # 2.) f[i][不偷編號 i-1 的房子] = max(f[i-1][偷編號 i-2 的房子], f[i-1][不偷編號 i-2 的房子])
        # 觀察 1. & 2. 發現有迭代關係，可以把 2 改寫成
        # f[i][不偷編號 i-1 的房子] = max( f[i-2][不能偷編號 i-3 的房子] + nums[i-1], f[i-1][不偷編號 i-2 的房子])
        # 這時候偷或不偷的標示，都是變成不偷，就可以拿掉，改寫成
        # f[i] = max(f[i-2]+nums[i-1], f[i-1])

        for i in range(3, len(nums) + 1): # 前兩棟房子已經在初始條件中設好了，所以從第三棟房子開始計算
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[len(nums)]
