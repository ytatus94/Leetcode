from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        # write your code here
        if grid is None:
            return 0
        m_rows = len(grid) # row

        if len(grid[0]) is None:
            return 0
        n_cols = len(grid[0]) # column

        # 狀態方程 f[i][j] 表示從 (0, 0) 走到 (i, j) 的 minimum path sum
        f = [[0 for j in range(n_cols)] for i in range(m_rows)]

        # 初始化
        f[0][0] = grid[0][0]
        # 最上面的 row 只能由左邊的點向右走
        for j in range(1, n_cols):
            f[0][j] = f[0][j-1] + grid[0][j]
        # 最左邊的 column 只能由上面的點向下走
        for i in range(1, m_rows):
            f[i][0] = f[i-1][0] + grid[i][0]

        # DP
        # 只能從上面往下走 (i-1, j) --> (i, j)
        # 或是從左邊往右邊走 (i, j-1) --> (i, j)
        # 選比較小的那一條路徑走
        for i in range(1, m_rows):
            for j in range(1, n_cols):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]

        return f[m_rows-1][n_cols-1]

# 方法 2:
from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        # write your code here
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0

        f = [[float('inf') for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                # f[0][0] = 1
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                    continue # 一定要有這一個 continue

                temp = float('inf')
                if i > 0: # first column can enter this 
                    temp = min(temp, f[i-1][j])
                if j > 0: # first row can enter this
                    temp = min(temp, f[i][j-1])

                f[i][j] = temp + grid[i][j]

        return f[m-1][n-1]

                
