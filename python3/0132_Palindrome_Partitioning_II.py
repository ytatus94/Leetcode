class Solution:
    def minCut(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        # 要找 minimum cut -> 如果 s 已經是 palindrome 就不需要 cut
        if s == s[::-1]:
            return 0

        # 如果只砍一刀就能變 palindrome
        #  s1=s[]0:i] s2=s[i+1:] 分別都是 palindrome
        for i in range(len(s)):
            s1 = s[:i] # 前半段
            s2 = s[i:] # 後半段
            if s1 == s1[::-1] and s2 == s2[::-1]:
                return 1

        # 砍兩刀以上的情形
        # s 的前 i 個字元最少可以被分成 dp[i] 個 palindromes
        dp = [i for i in range(len(s) + 1)]
        # 先初始化成最大值，雖然可以用 float('inf')，但是單看每個字元的時候，都是 palindrome
        # 所以一個長度為 n 的 string 最多就是能有 n 個 palindrome substring
        # 例如 aab 砍成 a, a, b -> 3 個 palindrome
        #     abacc 砍成 a, b, a, c, c -> 5 個 palindrome

        dp[0] = 0 # 前 0 個字元有 0 個 palindrome

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i: j + 1]
                if substring == substring[::-1]:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
    
        return dp[len(s)] - 1 # dp 是有幾個 palindrome 所以要砍 dp - 1 刀
