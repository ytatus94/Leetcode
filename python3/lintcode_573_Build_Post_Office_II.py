class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if grid is None or len(grid[0]) == 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        # 先把每個點的距離之和和訪問次數初始化為 0
        distance_sum = [[0 for col in range(cols)] for row in range(rows)]
        visited = [[0 for col in range(cols)] for row in range(rows)]
        
        # 先把所有的房子和空地的座標放入 houses 與 empties 中
        houses, empties = self.get_coordinatese(grid)

        # 從每一個房子來做 BFS 記錄到其他點的距離，還有拜訪次數
        for house in houses:
            self.bfs(house, grid, distance_sum, visited)
        
        # 看空地
        # 如果空地的訪問次數等於房子的數目，表示每個房子都可以拜訪到空地
        # 只要選出屬於這類的空地之中，和房子之間的距離之和最小的
        shortest_distance = sys.maxsize
        for empty in empties:
            x = empty[0]
            y = empty[1]
            if visited[x][y] == len(houses):
                shortest_distance = min(shortest_distance, distance_sum[x][y])
        
        if shortest_distance != sys.maxsize:
            return shortest_distance
            
        return -1
        
    def get_coordinatese(self, grid):
        self.WALL = 2
        self.HOUSE = 1
        self.EMPTY = 0
        
        houses, empties = list(), list()
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == self.HOUSE:
                    houses.append((row, col))
                if grid[row][col] == self.EMPTY:
                    empties.append((row, col))
        
        return houses, empties
        
    def bfs(self, house, grid, distance_sum, visited):
        rows = len(grid)
        cols = len(grid[0])
        
        queue = [(house[0], house[1], 0)] # x, y, dist
        hash = [[False for col in range(cols)] for row in range(rows)]
        hash[house[0]][house[1]] = True # 訪問過的點就標記起來
        
        while queue:
            (x, y, dist) = queue.pop(0)
            distance_sum[x][y] += dist
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor_x = x + dx
                neighbor_y = y + dy
                
                if not self.is_valid_point(grid, neighbor_x, neighbor_y):
                    continue
                # 新的座標點是還沒有拜訪過的點 (把不是的 continue)
                if hash[neighbor_x][neighbor_y]:
                    continue
    
                queue.append((neighbor_x, neighbor_y, dist + 1))
                hash[neighbor_x][neighbor_y] = True
                visited[neighbor_x][neighbor_y] += 1
        
    # 這個答案會是對的，但是會超時
    # def bfs(self, house, grid, distance_sum, visited):
    #     # 座標變換數組
    #     dx = [1, -1, 0, 0]
    #     dy = [0, 0, 1, -1]
        
    #     rows = len(grid)
    #     cols = len(grid[0])
        
    #     # 每個座標點和房子的距離
    #     distance = [[0 for col in range(cols)] for row in range(rows)]
        
    #     queue = [house]
    #     hash = [house] # 用來記錄是否已經走過了該座標點
    #     while queue:
    #         for i in range(len(queue)): # 層級遍歷，所以要有這個迴圈
    #             (x, y) = queue.pop(0)
            
    #             for i in range(4):
    #                 neighbor_x = x + dx[i]
    #                 neighbor_y = y + dy[i]
                
    #                 if not self.is_valid_point(grid, neighbor_x, neighbor_y):
    #                     continue
    #                 # 新的座標點是還沒有拜訪過的點 (把不是的 continue)
    #                 if (neighbor_x, neighbor_y) in hash:
    #                     continue
                    
    #                 # 新的座標點要是都符合條件，就加入 queue 裡面
    #                 # 並且加到 hash 裡面做記錄表示走過了這一個點
    #                 queue.append((neighbor_x, neighbor_y))
    #                 hash.append((neighbor_x, neighbor_y))
    #                 distance[neighbor_x][neighbor_y] = distance[x][y] + 1
    #                 distance_sum[neighbor_x][neighbor_y] += distance[neighbor_x][neighbor_y]
    #                 visited[neighbor_x][neighbor_y] += 1

    def is_valid_point(self, grid, x, y):
        rows = len(grid)
        cols = len(grid[0])
        
        # 新的座標點符合 grid 的範圍內
        if 0 <= x < rows and 0 <= y < cols:
            # 新的座標點必須是空地
            return grid[x][y] == 0
            
        return False
