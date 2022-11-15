# 這題其實就是費柏納西數列
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n: int) -> int:
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1

        # f[i] 從上一個階梯移動到第 i 個階梯的方法數
        # 因為一次可以移動一步或是兩步，所以上一個階梯可能是 f[i-1] 或是 f[i-2]
        # 要求所有可能的方法數就相加

        f = [0 for i in range(n+1)] # 要移動到第 n 個階梯，所以要用 n+1 當上限
        # 初始化
        f[0] = 1
        f[1] = 1

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]

        return f[n]
