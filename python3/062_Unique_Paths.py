# lintcode 114
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 1 or n == 1:
            return 1
            
        rows = m
        cols = n
        # status
        f = [[None for col in range(cols)] for row in range(rows)]
        
        # initialize
        # 第一行和第一列都初始化為 1
        for row in range(rows):
            f[row][0] = 1
        for col in range(cols):
            f[0][col] = 1
            
        # function: top-down
        for row in range(1, rows):
            for col in range(1, cols):
                f[row][col] = f[row - 1][col] + f[row][col - 1]
                
        return f[rows - 1][cols - 1]
