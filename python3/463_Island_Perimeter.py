class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        perimeter = 0
        
        '''
        掃描每個點如果是 1 時，看上下左右有幾個 0 表示有幾個邊
        如果 1 是在 grid 的邊緣，那也要把邊記錄下來
        '''
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if row + 1 < rows:
                        if grid[row + 1][col] == 0:
                            perimeter += 1
                    if row - 1 > -1:
                        if grid[row - 1][col] == 0:
                            perimeter += 1
                    if col + 1 < cols:
                        if grid[row][col + 1] == 0:
                            perimeter += 1
                    if col - 1 > -1:
                        if grid[row][col - 1] == 0:
                            perimeter += 1
                    # 在邊緣的情形
                    if row == 0:
                        perimeter += 1
                    if row == rows - 1:
                        perimeter += 1
                    if col == 0:
                        perimeter += 1
                    if col == cols - 1:
                        perimeter += 1
        return perimeter
