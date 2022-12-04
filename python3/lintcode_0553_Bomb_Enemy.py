from typing import (
    List,
)

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def max_killed_enemies(self, grid: List[List[str]]) -> int:
        # write your code here
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0

        # 要分成上下左右來看，所以開 4 個 m x n array
        up = [[0 for col in range(n)] for row in range(m)]
        down = [[0 for col in range(n)] for row in range(m)]
        left = [[0 for col in range(n)] for row in range(m)]
        right = [[0 for col in range(n)] for row in range(m)]

        # 先看往上炸能炸死多少敵人，可以推廣至往下，往左，和往右
        # 假設每個格子都能放炸彈
        # 1. 格子是空: 炸死敵人數目 = 上一格能炸死的敵人數目
        # 2. 格子是敵人: 炸死敵人數目 = 上一格能炸死的敵人數目 + 1
        # 3. 格子是牆: 炸死敵人數目 = 0
        # 4. 如果是第一 row: (初始化)
        #    4a. 格子是空: 炸死敵人數目 = 0
        #    4b. 格子是敵人: 炸死敵人數目 = 1
        #    4c. 格子是牆: 炸死敵人數目 = 0

        for row in range(m):
            for col in range(n):
                if row == 0:
                    if grid[row][col] == 'E':
                        up[row][col] = 1
                    else:
                        up[row][col] = 0 # 不論格子是空或是牆， row = 0 時都無法再往上炸死敵人了
                    continue
                elif row > 0:
                    if grid[row][col] == '0':
                        up[row][col] = up[row - 1][col]
                    elif grid[row][col] == 'E':
                        up[row][col] = up[row - 1][col] + 1
                    elif grid[row][col] == 'W':
                        up[row][col] = 0
        
        # 看往下能炸死多少敵人時，row 要從最後一 row 往回 loop
        for row in range(m-1, -1, -1):
            for col in range(n):
                if row == m - 1:
                    if grid[row][col] == 'E':
                        down[row][col] = 1
                    else:
                        down[row][col] = 0 # 最後ㄧ row 無法再往下炸死敵人了
                elif row < m - 1:
                    if grid[row][col] == '0':
                        down[row][col] = down[row + 1][col] # 這邊是要往下炸，所以看得是下面一 row
                    elif grid[row][col] == 'E':
                        down[row][col] = down[row + 1][col] + 1
                    elif grid[row][col] == 'W':
                        down[row][col] = 0

        # 看往左能炸死多少敵人
        for row in range(m):
            for col in range(n):
                if col == 0:
                    if grid[row][col] == 'E':
                        left[row][col] = 1
                    else:
                        left[row][col] = 0 # 第一 col 無法再往左炸死敵人了
                elif col > 0:
                    if grid[row][col] == '0':
                        left[row][col] = left[row][col - 1] # 這邊是要往左炸，所以看得是左邊的 col
                    elif grid[row][col] == 'E':
                        left[row][col] = left[row][col - 1] + 1
                    elif grid[row][col] == 'W':
                        left[row][col] = 0

        # 看往右能炸死多少敵人，所以右邊的 col 要先算，因此從 n-1 往左 loop
        for row in range(m):
            for col in range(n-1, -1, -1):
                if col == n - 1:
                    if grid[row][col] == 'E':
                        right[row][col] = 1
                    else:
                        right[row][col] = 0 # 最右邊的 col 無法再往右炸死敵人了
                elif col < n - 1:
                    if grid[row][col] == '0':
                        right[row][col] = right[row][col + 1] # 這邊是要往右炸，所以看得是右邊的 col
                    elif grid[row][col] == 'E':
                        right[row][col] = right[row][col + 1] + 1
                    elif grid[row][col] == 'W':
                        right[row][col] = 0

        max_kill = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0': # 只看空格放炸彈的情形
                    kill = up[row][col] + down[row][col] + left[row][col] + right[row][col]
                    max_kill = max(max_kill, kill)

        return max_kill
