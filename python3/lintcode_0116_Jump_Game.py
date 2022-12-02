# 方法1: 用 DP
from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False

        # 最後一個元素的 index = n-1
        # 假設在元素 index=i 如果能跳到最後一個元素
        # 那 a[i] >= (n-1) - i ==> 改寫成 a[i] + i >= n-1

        # 首先要能夠跳到第 i 個位置，然後計算從第 i 個位置上能跳耀到哪個位置
        f = [False] * len(a) # 用來記錄能不能跳到第 i 個位置
        # 初始化
        f[0] = True # 一開始就在元素 0 所以當然是 True

        for i in range(1, len(a)): # 要從元素 index=1 開始，因為 index=0 已經初始化了
            for j in range(i): # 對於所有 index 比 i 小的元素，只要有一個能跳到 i 就可以了
                if f[j] and a[j] + j >= i:
                    f[i] = True
                    break

        return f[len(a) - 1]

from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        # 開一個長度是 a 的數組
        f = [False for i in range(len(a))] # 問能不能，所以先初始化為 False

        # 初始化
        f[0] = True # 本來就在 first index of the array

        for i in range(len(a)): # i = 0 ~ len(a)-1
            for j in range(i): # 枚舉 i 之前的所有 index: 0 ~ i-1
                if f[j] == True and j + a[j] >= i: # 能跳到 j 且能從 j 跳到 i
                    f[i] = True
                    break # 只要 0 ~ i-1 中有一個能跳到 i 那就可以了

        return f[len(a) - 1]    

# 方法2: 用貪心法
from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False

        # 用來記錄目前最遠能跳到哪個 index
        max_index = a[0]

        for i in range(1, len(a)):
            if i <= max_index: # 表示能跳到 i
                # 如果能跳到 i，那就要看從 i 能跳到哪 index
                max_index = max(max_index, i + a[i]) # 更新 max_index

        if max_index >= len(a) - 1:
            return True
        return False
