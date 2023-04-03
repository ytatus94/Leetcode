# 會超時
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes is None or len(envelopes) == 0:
            return 0

        # 信封可能不按大小排列，所以要先排序
        envelopes = sorted(envelopes, key=lambda x: (x[0], x[1]))

        # 這一題其實是 LIS 的 2D 版本
        dp = [0 for _ in range(len(envelopes))]

        for i in range(len(envelopes)):
            dp[i] = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
