from typing import (
    List,
)

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longest_consecutive(self, num: List[int]) -> int:
        # write your code here
        if num is None or len(num) == 0:
            return 0

        # 不論連續上升或是連續下降都沒關係，反正排序後就只看連續上升
        # 可能會有重複的數值，所以取 set()
        num = sorted(set(num))

        # dp[i] = 直到 i 個元素為止，最長的連續子序列的長度
        dp = [0 for i in range(len(num))]
        # 初始條件: 每個元素自己都是一個連續子序列
        for i in range(len(num)):
            dp[i] = 1

        for i in range(len(num)):
            if num[i - 1] + 1 == num[i]:
                dp[i] = dp[i - 1] + 1

        return max(dp)
