class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 如果 s 本身就是 palindrome
        if s == s[::-1]:
            return s

        # dp[i][j] = 從 s[i]~s[j] 的最長 palindrome 長度
        # 因為子字串是 s[i]~s[j], 所以 j >= i，因此 dp[i][j<i]=0 (下三角形 = 0)
        dp = [[0 for j in range(len(s))] for i in range(len(s))]

        # 初始條件: 每個字母都是 palindrome --> dp[i][i] = 1
        for i in range(len(s)):
            dp[i][i] = 1

        longest_length = 0
        start = -1
        end = -1

        # 要倒著看
        for i in range(len(s) - 1, -1, -1):
            # 從 j=i+1 開始，因為 i=j 時 dp[i][j] = 1
            # 當 i+1 >= len(s) 的時候，不會進迴圈
            for j in range(i + 1, len(s)):
                # 先看 s[i]~s[j] 去頭或是去尾時，能形成的最大 palindrome 長度
                # s[i]~s[j] 去尾就是 s[i]~s[j-1]
                # s[i]~s[j] 去頭就是 s[i+1]~s[j]
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

                # 看看 s[i][j] 本身是不是 palindrome
                substring = s[i: j + 1]
                if substring == substring[::-1]:
                    dp[i][j] = max(dp[i][j], len(substring))

                    if longest_length < dp[i][j]:
                        longest_length = dp[i][j]
                        start = i
                        end = j

        if start != -1 and end != -1:
            result = s[start: end + 1]
        else:
            result = s[0]

        return result
