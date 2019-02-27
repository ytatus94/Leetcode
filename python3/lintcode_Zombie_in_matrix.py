class Coordinate:
    def __init__(x, y):
        self.x = x
        self.y = y
        
class Solution:
    PEPLE = 0
    ZOMBIE = 1
    WALL = 2
    
    deltaX = [1, 0, 0, -1]
    deltaY = [0, 1, -1, 0]
    
    def zombie(grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return None
            
        n = len(grid)
        m = len(grid[0])
        
        ppl = 0
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] = PEOPLE:
                    ppl += 1
                elif grid[i][j] == ZOMBIE:
                    queue.append(Coordinate(i, j))
                    
        if ppl == 0:
            return 0
        
        // BFS
        days = 0
        while queue:
            days += 1
            size = len(queue)
            for i in range(size):
                zb = queue.pop()
                for direction in range(4):
                    adj = Coordinate(zb.x + deltaX[direction], zb.y + deltaY[direction])
                    
                    if not isPeople(adj, grid):
                        continue
                        
                    grid[adj.x][adj.y] = ZOMBIE
                    ppl -= 1
                    
                    if ppl == 0:
                        return days
                        
                    queue.append()
        return -1
        
    def isPeople(coor, grid):
