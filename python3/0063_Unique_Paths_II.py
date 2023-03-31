class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return -1
            
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        grid = [[0 for col in range(cols)] for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    grid[row][col] = 0 # 把障礙點設成 0
                elif row == 0 and col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[rows - 1][cols - 1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 開一個二維陣列儲存走到 (i, j) 的方法數
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                # 先檢查是不是障礙物，如果是障礙物就不能走了，直接換下一個
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
