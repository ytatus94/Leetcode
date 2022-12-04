# 序列型 DP, 最值型 DP
# 轉移方程:
#   f[i] = max( 1, f[i-1]+1|j>0 and a[i-1]<a[i])
#   f[i] = 以 a[i] 結尾的最長連續上升子序列長度
#   case 1.) 1: 子序列只有 a[i] 自己
#   case 2.) f[i-1]+1 = 以 a[i-1] 結尾的最長連續上升子序列長度，再加上 a[i]
# 初始條件: 沒有初始條件
# TC = O(N), SC=O(N) (其實 SC 是 2N) 可以用滾動數組優化成 SC = O(1)

# 方法 1: TC = O(N), SC=O(N) (其實 SC 是 2N)
from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        # write your code here
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return 1

        # 題目說連續上升子序列可以由左往右，也能由右往左
        # 所以要從原本的序列中找連續上升子序列或連續下降子序列

        # 開兩個數組保存以 i 結為的上升/下降子序列的長度
        f = [0 for i in range(len(a))] # 上升序列
        g = [0 for i in range(len(a))] # 下降序列

        for i in range(len(a)):
            if i == 0:
                f[0] = 1
                g[0] = 1
            elif i > 0:
                f[i] = 1
                g[i] = 1
                if a[i] > a[i - 1]:
                    f[i] = f[i - 1] + 1
                if a[i] < a[i - 1]:
                    g[i] = g[i - 1] + 1

        maxF = max(f) # 找出連續上升子序列中最大的
        maxG = max(g) # 找出連續下降子序列中最大的

        return max(maxF, maxG)

# 方法 2:
from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        # write your code here
        if len(a) == 0:
            return 0

        res1 = self.LIS(a, len(a))

        # 手動把 array 顛倒 (一定要會)
        i, j = 0, len(a) - 1
        while i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
            j -= 1

        # 這時候 a 已經 reverse 了
        res2 = self.LIS(a, len(a))

        # return res1 > res2 ? res1 : res2 # python 會有 syntax error
        if res1 > res2:
            return res1
        else:
            return res2

    def LIS(self, a: List[int], n: int) -> int:
        f = [0 for i in range(n)]
        res = 0
        for i in range(len(a)):
            f[i] = 1
            if i > 0 and a[i] > a[i - 1]:
                f[i] = f[i - 1] + 1
            res = max(res, f[i])
        return res

# 方法 3: 滾動數組 TC=O(n), SC=O(1)
from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        # write your code here
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return 1

        # 因為題目說可以 from right to left or from left to right
        # 看以 ai 元素結尾的最長的連續上升 (right to left) 
        # 和連續下降 (left to right) 子序列長度，然後選出最長的那個
        longest = 0
        dp_lr = 1 # 此時是 index=0 時的最長連續上升子序列長度
        dp_rl = 1 # 此時是 index=1 時的最長連續下降子序列長度

        for i in range(1, len(a)): # index 從 1 開始才能避免 i-1 < 0 的情況
            # from left to right (連續上升)
            if a[i] > a[i - 1]:
                dp_lr = dp_lr + 1
            else:
                dp_lr = 1

            # from right to left (連續下降)
            dp_rl = dp_rl + 1 if a[i] < a[i - 1] else 1

            longest = max(longest, max(dp_lr, dp_rl))

        return longest
