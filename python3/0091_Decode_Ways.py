class Solution:
    def numDecodings(self, s: str) -> int:
        # 開一個一維陣列紀錄從 s[0] 到 s[i] 解密的方法數
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if int(s[i]) != 0:
                    dp[i] = 1 # 第一個元素不是 0 時，只有一種方式解密
                else:
                    dp[i] = 0 # 第一個元素是 0 時，無法解密
            else:
                # 只把 s[i] 對應一個字母
                if int(s[i]) != 0:
                    dp[i] += dp[i - 1]
                # 把 s[i-1]s[i] 對應一個字母
                if 10 <= int(s[i - 1] + s[i]) <= 26:
                    if i == 1:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i - 2]
        return dp[len(s) - 1]
