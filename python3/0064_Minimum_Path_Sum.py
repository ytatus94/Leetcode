class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        # 每一個節點的最小路徑和，是來自於上面或是左邊的節點的最小路徑和加上自己
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col > 0:
                    grid[row][col] += grid[row][col - 1]
                elif col == 0 and row > 0:
                    grid[row][col] += grid[row - 1][col]
                elif row > 0 and col > 0:
                    grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
                    
        return grid[rows - 1][cols - 1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 開一個二維陣列紀錄到 (i, j) 的最小路徑和
        dp = [[0] * n] * m
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0: # 只能從左邊一格走過來
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0: # 只能從上面一格走過來
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]

# lintcode 110
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return -1
            
        if grid[0] is None or len(grid[0]) == 0:
            return -1
            
        # status
        rows = len(grid)
        cols = len(grid[0])
        f = [[None for col in range(cols)] for row in range(rows)]
        
        # initialize
        # 初始化第一列
        f[0][0] = grid[0][0]
        for col in range(1, cols):
            f[0][col] = grid[0][col] + f[0][col - 1]
        # 初始化第一欄
        for row in range(1, rows):
            f[row][0] = grid[row][0] + f[row - 1][0]
        
        # function: top-down
        for row in range(1, rows):
            for col in range(1, cols):
                f[row][col] = grid[row][col] + min(f[row - 1][col], f[row][col - 1])
                
        # answer
        return f[rows - 1][cols - 1]
