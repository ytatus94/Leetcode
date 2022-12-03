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

