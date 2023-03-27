# 座標型 DP, 最值型 DP
# 轉移方程:
#   f[i][j] = min( f[i-1][j], f[i][j-1] ) + A[i][j]
#   f[i][j] = 從 (0, 0) 到 (i, j) 的最小路徑數字和
# 初始條件:
#   f[0][0] = A[0][0]
# 邊界情況:
#   f[0][j] = f[0][j-1] + A[0][j] | j>0
#   f[i][0] = f[i-1][0] + A[i][0] | i>0
# TC = O(MN) SC = O(MN) 用滾動數組時 SC = O(1)

# 方法 1:
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

# 如果要把路徑印出來的話
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
        if m == 0:
            return 0

        f = [[float('inf') for col in range(n)] for row in range(m)]

        # 開一個 policy 數組紀錄上一個 minimum path sum 是從哪裡來的
        # pi[i][j] = 0: 從上面來
        # pi[i][j] = 1: 從左邊來
        pi = [[-1 for col in range(n)] for row in range(m)] # 用一個不是 0 或 1 的數來初始化

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    f[row][col] = grid[row][col]
                    continue

                temp = float('inf')
                if row > 0:
                    temp = min(temp, f[row - 1][col])
                    if temp == f[row - 1][col]:
                        pi[row][col] = 0
                if col > 0:
                    temp = min(temp, f[row][col - 1])
                    if temp == f[row][col - 1]:
                        pi[row][col] = 1

                f[row][col] = temp + grid[row][col]

        # 然後由後往前找出 path (因為 pi 記錄的是"上一個"來自哪)
        path = [-1 for i in range(m + n - 1)]
        x = m - 1
        y = n - 1
        for p in range(m + n - 1):
            path[p] = grid[x][y]
            if pi[x][y] == 0:
                x -= 1
            else:
                y -= 1
        # path 中存的是相反的順序，印出來要反著印，就變正的順序
        for p in range(m + n - 2, -1, -1):
            print(path[p])

        return f[m - 1][n - 1]    
    
# 方法 3:
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

        # Create a m*n array to save the minimum path sum
        # dp[i][j] means minimum path sum from (0, 0) to (i, j)
        dp = [[0 for col in range(n)] for row in range(m)]

        dp[0][0] = grid[0][0]

        for row in range(m):
            for col in range(n):
                dp[row][col] = grid[row][col]
                if row == 0 and col == 0:
                    continue
                if row == 0:
                    dp[row][col] += dp[row][col - 1]
                    continue
                if col == 0:
                    dp[row][col] += dp[row - 1][col]
                    continue
                dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])

        print(dp)

        return dp[m - 1][n - 1]

# 方法 4: 用滾動數組
# 把方法 3 中的 i --> new, i-1 --> old 就好
# 注意只能改 f 的，不能改 grid 的
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

        # 因為f[i][j] 只和 f[i-1][j] 與 f[i][j-1] 有關
        # 所以只需要開 2 dim array 然後用滾動數組計算
        f = [[float('inf') for j in range(n)] for i in [0, 1]]

        # two pointers
        # where is row i stored: new
        # where is row i-1 stored: old = 1 - new
        old = None
        new = 0
        for i in range(m):
            # swap old and new
            old = new
            new = 1 - new # 0 --> 1, 1 --> 0
            for j in range(n):
                # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                # f[0][0] = 1
                if i == 0 and j == 0:
                    f[new][j] = grid[i][j]
                    continue # 一定要有這一個 continue

                temp = float('inf')
                if i > 0: # first column can enter this 
                    temp = min(temp, f[old][j])
                if j > 0: # first row can enter this
                    temp = min(temp, f[new][j-1])

                f[new][j] = temp + grid[i][j]

        # 當離開迴圈時，最後一 row 剛好是 new
        return f[new][n-1]

    
# 方法 5: 另一種滾動數組的寫法
# 把方法 4 中的 new --> i%2, old --> 1 - i%2
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

        # 因為f[i][j] 只和 f[i-1][j] 與 f[i][j-1] 有關
        # 所以只需要開 2 dim array 然後用滾動數組計算
        f = [[float('inf') for j in range(n)] for i in [0, 1]]

        # two pointers
        # where is row i stored: new
        # where is row i-1 stored: old = 1 - new
        for i in range(m):
            for j in range(n):
                # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
                # f[0][0] = 1
                if i == 0 and j == 0:
                    f[i % 2][j] = grid[i][j]
                    continue # 一定要有這一個 continue

                temp = float('inf')
                if i > 0: # first column can enter this 
                    temp = min(temp, f[1 - (i % 2)][j])
                if j > 0: # first row can enter this
                    temp = min(temp, f[i % 2][j-1])

                f[i % 2][j] = temp + grid[i][j]

        # 當離開迴圈時，最後一 row 剛好是 new
        return f[(m - 1) % 2][n-1]

