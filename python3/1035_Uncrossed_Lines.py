class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        # dp[i][j] = nums1 的前 i 個元素和 nums2 的前 j 個元素最多能有多少條線不相交 
        # 初始條件:
        # dp[i=0][j] = 0, nums1 的前 0 個元素當然沒和 nums2 的元素連線
        # dp[i][j=0] = 0, nums2 的前 0 個元素沒辦法和 nums1 的元素連線
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n][m]
