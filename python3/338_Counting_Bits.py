class Solution:
    def countBits(self, n: int) -> List[int]:
        # f[i] 表示數字 i 的二進位有多少個 1
        f = [0 for i in range(n+1)]
        # 初始化
        f[0] = 0 # 數字 0 有 0 個 1

        # i%2 表示數字 i 變成二進制後最後的數是不是 1
        # i >> 1 就是二進制的右移，相當於把 i 變成 floor(i/2)
        for i in range(1, n+1):
            f[i] = (i % 2) + f[i >> 1]

        return f
