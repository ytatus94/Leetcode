# 序列型 DP, 最值型 DP
# 轉移方程:
#   f[i] = min(f[i-1], f[i-2]+A[i-1])
#   f[i] = 偷前 i 棟房子能得到的最大金額
# 初始條件:
#   f[0] = 0, f[1] = A[0]
# TC = O(N), SC = O(1)
# 這一題基本上和 house robber 一樣，唯一的差別是頭尾連再一起了，
# 所以要把頭尾分開討論，斷開成兩個單獨的序列，就可以用 house robber 了

from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def house_robber2(self, nums: List[int]) -> int:
        # write your code here
        if nums is None:
            return 0
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # 第一間房子 index = 0
        # 最後一間房子 index = n-1
        # 現在兩間房子相鄰，所以不能同時偷這兩間
        # 不偷第一間-->變成房子 1~n-1 的 house robber 1
        # 不偷最後一間-->變成房子 0~n-2 的 hourse robber 1
        # 所以分開成這兩種情形討論

        res1 = self.house_robber1(nums[1:])
        res2 = self.house_robber1(nums[:-1])

        return max(res1, res2)

    def house_robber1(self, nums: List[int]) -> int:
        # 這裡就是 house robber 原封不動的抄過來
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        f = [0 for i in range(n + 1)]
        
        old = 0 # f[0]
        new = nums[0] # f[1]
        
        for i in range(2, n+1): # 注意是從 2 開始
            # f[i-1] --> new
            # f[i-2] --> old
            temp = max(new, old + nums[i - 1])
            old = new
            new = temp
        return new
