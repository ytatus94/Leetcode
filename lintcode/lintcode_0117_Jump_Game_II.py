# 方法1: dp，會超時 TC=O(n^2), SC=O(n)
from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a: List[int]) -> int:
        # write your code here
        if a is None or len(a) == 0:
            return 0

        # f[i] 表示跳到 index=i 所需要的最小跳耀步數
        f = [float('inf')] * len(a)

        # 初始化
        f[0] = 0 # 一開始在 index=0 不需要跳，所以 0 步

        for i in range(1, len(a)):
            for j in range(0, i): # 從所有比 i 小的 index 中，找出能跳到 i 的 index 並且查看步數要幾步，紀錄步數最小的那個是幾步
                if a[j] + j >= i: # 能跳到 i
                    f[i] = min(f[i], f[j] + 1) # f[j] 是能跳到 j 需要的最小步數，因為從 j 跳到 i 還要再多一步所以 +1

        return f[len(a)-1]

# 方法2: 貪心法
from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a: List[int]) -> int:
        # write your code here
        end = 0 # 上一步所能達到的最遠 index
        max_jump = 0 # 當前 index 所能達到的最遠 index
        count = 0 # 要跳幾步

        # 不可以包含最後一個點，因為只要能跳到最後一個點就好
        # 如果包含的話，會被多計算多跳一步
        for i in range(len(a) - 1): 
            max_jump = max(max_jump, a[i] + i)
            # 如果當前的 index 正好是上一步的能跳到的最遠 index 了
            # 那就要再多跳一步才能達到當前 index 所能達到的 max_jump 位置
            if end == i:
                end = max_jump
                count += 1
        return count

# 方法3: 貪心法
from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a: List[int]) -> int:
        # write your code here
        p = [0]
        for i in range(len(a) - 1):
            while(i + a[i] >= len(p) and len(p) < len(a)):
                p.append(p[i] + 1)

        return p[-1]

