# lintcode 111
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        # 第 i 階的方法數 = 第 i - 1 階的方法數 + 第 i - 2 階的方法數
        # 其實就是費伯納西數列
        if n <= 1:
            return n
            
        # 初始條件
        #           ___
        #          | 2 第 2 階可以從第 0 階直接上來，也可以從第 1 階上來，兩種方法
        #      ____|
        #     | 1 第 1 階也只有一種
        #  ___|
        #   1 第 0 階只有一種
        #
        pre = 1
        pre_pre = 1
        count = 0
        for i in range(2, n + 1):
            count = pre + pre_pre
            pre_pre = pre
            pre = count
        return count
