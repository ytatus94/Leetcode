# 方法 1:
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
