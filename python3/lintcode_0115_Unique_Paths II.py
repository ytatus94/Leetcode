from typing import (
    List,
)

class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        # write your code here

        # 和 unique paths 一樣，只是多了不能走的格子
        # 所以轉移方程 f[i][j] = 從左上角走到 (0, 0) 有幾種方式
        # 1. 不能走的格子 f[i][j] = 0
        # 2. 起點 f[0][0] = 1 (前提是起點不是不能走的格子)
        # 3. i = 0 或 j = 0 時 f[i][j] = 1 (前提是格子要能走)
        # 3. 其他能走的格子 f[i][j] = f[i-1][j] + f[i][j-1]

        m = len(obstacle_grid)
        n = len(obstacle_grid[0])

        # 如果起點或終點不能走，直接結束
        if obstacle_grid[0][0] == 1 or obstacle_grid[m-1][n-1] == 1:
            return 0

        # 開一個 m x n 的 array 因為要計算幾種方式，所以先初始化 = 0
        f = [[0 for col in range(n)] for row in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    f[row][col] = 1 # 先把最上面的 row 和最左邊的 column 初始化 = 1

                if obstacle_grid[row][col] == 1:
                    f[row][col] = 0 # 再把不能走的格子初始化 = 0
                    # 如果這時候 row = 0 or col = 0 就會被覆蓋 

                # 到這邊可能有一種情況是 row = 0 或 col = 0 但是它的前一格不能走
                # 這時候這種格子也要是 f[i][j] = 0
                if row == 0 and col > 0 and f[row][col - 1] == 0:
                    f[row][col] = 0
                if col == 0 and row > 0 and f[row - 1][col] == 0:
                    f[row][col] = 0

                if row > 0 and col > 0 and obstacle_grid[row][col] == 0:
                    f[row][col] = f[row - 1][col] + f[row][col - 1]
        print(f)
        return f[m-1][n-1]
