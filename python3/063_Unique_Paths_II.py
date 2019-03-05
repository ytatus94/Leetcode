# lintcode 115
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
