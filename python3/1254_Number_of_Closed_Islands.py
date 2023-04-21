class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        self.visited = [[False for j in range(cols)] for i in range(rows)]
        count = 0

        # 先用 BFS 找到島嶼
        # 再判斷島嶼是否是 closed 的
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and not self.visited[row][col]:
                    is_closed = self.bfs(grid, row, col)
                    if is_closed:
                        count += 1

        return count

    def bfs(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        queue = [(row, col)]

        is_closed = True

        while queue:
            r, c = queue.pop(0)
            self.visited[r][c] = True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row = r + dr
                next_col = c + dc

                # 如果由 (r, c) 衍生出來的鄰居已經超出邊界了
                # 表示 (r, c) 就在邊界上，所以不是 closed 的
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    is_closed = False
                    continue

                if self.visited[next_row][next_col]:
                    continue

                if grid[next_row][next_col] == 0:
                    queue.append((next_row, next_col))
                    self.visited[next_row][next_col] == True # 走過就標記起來

        return is_closed
