# 座標型 DP, 計數型 DP
# 轉移方程: f[i][j] = f[i-1][j] + f[i][j-1]
# TC = O(MN), SC = O(MN)

# 方法 1:
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


# 方法 2:
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def unique_paths(self, m: int, n: int) -> int:
        # write your code here
        # 開一個 m x n 的數組
        f = [[0 for col in range(n)] for row in range(m)]

        # 初始化:
        # f[0][0] = 1 本來就在 (0, 0) 這一格，所以一種方法
        # 邊界情況:
        # 最上面一 row (m = 0) 的每一格，都只能由左邊那格走來
        # 最左邊一 column (n = 0) 的每一格，都只能由上面那格走來
        # 所以只有一種方式
        # f[0][0 ~ n-1] = 1 且 f[0 ~ m-1][0] = 1

        # 轉移方程: 其他格子點，可以從左邊那格走來也可以從上面那格走來
        # f[i][j] = f[i-1][j] + f[i][j-1]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    f[row][col] = 1
                else:
                    f[row][col] = f[row - 1][col] + f[row][col - 1]

        return f[m - 1][n - 1]
