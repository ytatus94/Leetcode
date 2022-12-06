# 劃分型 DP, 最值型 DP
# 轉移方程
#   f[i] = min_{1<=j*J<=i}(f[i-j*j]+1)
# 初始條件:
#   f[0] = 0
# TC = O(N^1.5), SC = O(N)

class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def num_squares(self, n: int) -> int:
        # write your code here

        # 先看看 n 是不是完全平方數
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
        # # 初始條件
        f[0] = 0

        for i in range(1, n + 1):
            for j in range(i+1): # j 最大可以等於 i
                if i - j * j >= 0:
                    f[i] = min(f[i], f[i - j*j] + 1)
        
        return f[n]
        
