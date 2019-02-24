class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if grid is None or len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        # 用來標記有沒有走過該點
        self.visited = [[False for col in range(cols)] for row in range(rows)]
        
        # 迴圈所有的點
        # 如果找到 1 的點，又是還沒訪問過的，就由該點做 BFS
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not self.visited[row][col]:
                    # 每一個點要跑一次 BFS
                    self.bfs(grid, row, col)
                    count += 1
                    
        return count
                    
    def bfs(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])
        
        queue = [(row, col)]
        
        while queue:
            x, y = queue.pop(0)
            self.visited[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor_x = x + dx
                neighbor_y = y + dy
                                
                # 鄰居不可以超過矩陣的範圍
                if not(0 <= neighbor_x < rows and 0 <= neighbor_y < cols):
                    continue
                
                # 鄰居必須是還沒有拜訪過的點
                if self.visited[neighbor_x][neighbor_y]:
                    continue
                
                if grid[neighbor_x][neighbor_y] == '1':
                    queue.append((neighbor_x, neighbor_y))
                    self.visited[neighbor_x][neighbor_y] = True

 # lintcode 433
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        island_counts = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    self.bfs(grid, row, col)
                    island_counts += 1
                    
        return island_counts
        
    def bfs(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])
        
        # 座標變換數組
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        queue = [(row, col)]
        grid[row][col] = 0 # 用過的點就標記成 0
        
        while queue:
            origin = queue.pop(0)
            x = origin[0]
            y = origin[1]
            for i in range(4):
                neighbor_x = x + dx[i]
                neighbor_y = y + dy[i]
                neighbor = (neighbor_x, neighbor_y)
                
                if not (0 <= neighbor_x < rows and 0 <= neighbor_y < cols):
                    continue
                
                if grid[neighbor_x][neighbor_y]:
                    queue.append(neighbor)
                    grid[neighbor_x][neighbor_y] = 0
