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

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes is None or len(envelopes) == 0:
            return 0

        # 信封可能不按大小排列，所以要先排序
        # 把 w 遞增排序，h 遞減排序
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        # 排序後可以把 2D LIS 簡化成 1D LIS
        # 至於為什麼 h 要遞減排序是因為當 w 相同時 (w, h小) 無法放入 (w, h大) 中，只能選一個放
        # 單看 h 的序列的話 [h小, h大] 會使 len(LIS)=2 但這不是正確答案
        # 如果排序成 [h大, h小], 那 len(LIS)=1 就會是正確的

        nums = [h for w, h in envelopes]
        res = self.LIS(nums)
        return res

    def LIS(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                insert_index = self.binary_search(dp, nums[i])
                dp[insert_index] = nums[i]

        return len(dp)

    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid

        if nums[start] < target:
            return start + 1
        elif nums[start] >= target:
            return start
