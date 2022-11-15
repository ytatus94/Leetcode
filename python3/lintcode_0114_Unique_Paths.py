class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def unique_paths(self, m: int, n: int) -> int:
        # write your code here
        if m == 1 or n == 1:
            return 1

        # f[i][j] 表示從 (0, 0) 移動到 (i, j) 的方法數
        f = [[0 for col in range(n)] for row in range(m)]
        # 初始化，第一 row 和第一 column 上的每個格子都只有一種方式能抵達
        for row in range(m):
            f[row][0] = 1
        for col in range(n):
            f[0][col] = 1

        # 除了第一 row 和第一 column 的其他格子，都可以由上方或是左方移動過來
        # 所以要把上方和左方的方法數相加
        for row in range(1, m):
            for col in range(1, n):
                f[row][col] = f[row-1][col] + f[row][col-1]

        return f[m-1][n-1]

