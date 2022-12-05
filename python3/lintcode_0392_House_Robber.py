# 序列型 DP, 最值型 DP
# 轉移方程:
#   f[i] = max( f[i-1], f[i-2]+A[i-1] )
#   f[i] = 偷前 i 棟房子能得到的最大金額
# 初始條件:
#   f[0] = 0
#   f[1] = A[0]
#   f[2] = max(A[0], A[1])
# TC = O(N), SC = O(1) (用滾動數組)

# 方法 1:
from typing import (
    List,
)

class Solution:
    """
    @param a: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def house_robber(self, a: List[int]) -> int:
        # write your code here
        if a is None:
            return 0
        n = len(a) # number of houses
        if n == 0:
            return 0
        if n == 1:
            return a[0]

        # 本來要開一個數組紀錄偷前 i 棟房子能得到的最大金額
        # 並且記錄最後一棟房子 i-1 要不要偷
        # 第二個參數 0 表示不偷房子 i-1, 1 表示要偷房子 i-1 
        # case 1.) 不偷房子 i-1 這時候房子 i-2 可以偷也可以不偷
        # f[i][0] = max(f[i-1][0], f[i-1][1])
        # case 2.) 偷房子 i-1 那就不能偷房子 i-2 
        # f[i][1] = f[i-1][0] + A[i-1] (A[i-1]是房子 i-1 中有多少錢)

        # 歸納後得到
        # 不偷房子 i-1 那 f[i] = f[i-1]
        # 要偷房子 i-1 那 i-2 不能偷 f[i] = f[i-2] + A[i-1]
        # 轉移方程:
        # f[i] = 偷前 i 棟房子能得到的最大金額
        #      = max(不偷房子 i-1, 要偷房子 i-1)
        #      = max(f[i-1], f[i-2]+A[i-1])

        # Create an array to save the maximum money can be robbed
        # from the first i houses
        f = [0 for i in range(n + 1)]

        # initial condition:
        f[0] = 0 # rob first 0 house, get 0 money
        f[1] = a[0] # rob the first 1 house can get maximum money a[0]
        # 只有一棟房子能偷，可以偷可以不偷，能偷到的最大金額就是要偷
        f[2] = max(a[0], a[1]) # 其實可以不要這一行
        # 有兩棟房子能偷，可以偷到的最大金額就是偷其中一棟

        for i in range(3, n + 1): # 注意從 3 開始 (如果不要 f[2] 那這裡就從 2 開始)
            f[i] = max(f[i-1], f[i-2] + a[i-1])

        return f[n]
    
# 方法 2: 用滾動數組
from typing import (
    List,
)

class Solution:
    """
    @param a: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def house_robber(self, a: List[int]) -> int:
        # write your code here
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return a[0]

        # Create an array to save the maximum money for the first i houses
        f = [0 for i in range(n + 1)]

        # use rolling variables
        # initial conditions:
        old = 0 # f[0] = 0, rob 0 hourse get nothing
        new = a[0] # f[1] = a[0], rob first house get a[0]

        for i in range(2, n + 1):
            t = max(new, old + a[i-1])
            old = new
            new = t

        # when leaving for loop, the i = n, and new is f[n]
        return new
