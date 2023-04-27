# 劃分型 DP, 最值型 DP
# 轉移方程
#   f[i] = min_{1<=j*J<=i}(f[i-j*j]+1)
# 初始條件:
#   f[0] = 0
# TC = O(N^1.5), SC = O(N)

# 超時
class Solution:
    def numSquares(self, n: int) -> int:
        # 對於每一個整數 n 都可以由 n 個 1 的和組成，而 1 是完全平方數
        # 因此整數 n 最多可由 n 個完全平方數的和組成

        # i "最少"由 dp[i] 個完全平方數之和組成
        # 所以初始化成最大值，這邊可以用 float('inf') 或是 i 自己
        dp = [i for i in range(n + 1)]

        # 初始化
        dp[0] = 0
        for i in range(1, n + 1):
            if i * i <= n:
                dp[i * i] = 1

            # j 不可以 loop 到 i (這樣寫記憶體會超過)
            # for j in range(1, i):
            #     if j * j <= i:
            #         dp[i] = min(dp[i], dp[i - j * j] + 1)
            
            sqrt = int(i ** 0.5)
            for j in range(1, sqrt + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]

# 超出記憶體
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def num_squares(self, n: int) -> int:
        # write your code here
        f = [float('inf') for i in range(n + 1)]
        f[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                f[i] = min(f[i], f[i - j * j] + 1)
                j += 1
                
        return f[n]

# 超出記憶體
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def num_squares(self, n: int) -> int:
        # write your code here
        sqrt_n = int(n**0.5)
        if sqrt_n * sqrt_n == n:
            return 1
        
        # n 可以寫成完全平方數的和
        # n = a0 + a1 + ... + ai
        # 其中 aj = 完全平方數
        # 所以 ai 是完全平方數，n - ai = a0 + ... + ai-1 也是完全平方數
        # 找 f[n] = min(f[n-ai] + 1)

        # f[i] = i 最少被分成幾個完全平方數的和
        f = [float('inf') for i in range(n + 1)]
        # 初始條件
        f[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i: # j^2 最大可以等於 i
                f[i] = min(f[i], f[i - j*j] + 1)
                j += 1
        
        return f[n]
        
