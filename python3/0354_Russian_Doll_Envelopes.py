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

# 要先排序！先把 w 遞增排序，再把 h 遞減排序
# 先把 w 遞增排序後，題目變成找 h 的 LIS
# 但是當 w 相同時，如果 h1 < h2: [(w, h1), (w, h2)] 這樣子看 h 的 LIS 時會被當成 (w, h1) 可以放到 (w, h2) 裡面
# 因此要把 h 做遞減排序，[(w, h2), (w, h1)] 就不會把 (w, h1) 當成能放入 (w, h2) 裡面了
