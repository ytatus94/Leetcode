class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        self.visited = [[False for j in range(cols)] for i in range(rows)]

        # 用 BFS 找出島嶼
        # 先找出有和邊邊連接的島嶼
        for r in range(rows):
            if grid[r][0] == 1 and not self.visited[r][0]:
                self.bfs(grid, r, 0)
            if grid[r][cols - 1] == 1 and not self.visited[r][cols - 1]:
                self.bfs(grid, r, cols - 1)

        for c in range(cols):
            if grid[0][c] == 1 and not self.visited[0][c]:
                self.bfs(grid, 0, c)
            if grid[rows - 1][c] == 1 and not self.visited[rows - 1][c]:
                self.bfs(grid, rows - 1, c)

        # 剩下還沒 visited 的島嶼就是 isolated 的
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not self.visited[r][c]:
                    count += 1

        return count

    def bfs(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        queue = [(row, col)]

        while queue:
            r, c = queue.pop(0)
            self.visited[r][c] = True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row = r + dr
                next_col = c + dc

                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue

                if self.visited[next_row][next_col]:
                    continue

                if grid[next_row][next_col] == 1:
                    queue.append((next_row, next_col))
                    self.visited[next_row][next_col] = True
