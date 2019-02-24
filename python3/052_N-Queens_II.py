class Solution:
    def totalNQueens(self, n: 'int') -> 'int':
        res = []
        if n <= 0:
            return res
        pos = [] # 紀錄 Q 的位置，index 是 row 的值，value 是 col 的值
        self.dfs(n, res, pos)
        return len(res)
    
    def dfs(self, n, res, pos):
        if len(pos) == n:
            res.append(pos[:])
            return
        for col in range(n):
            # 兩個 Q 不可以在同一 row, col, 和對角線上
            if self.is_diagonal(pos, col):
                continue
            pos.append(col)
            self.dfs(n, res, pos)
            pos.pop()
    
    def is_diagonal(self, pos, col):
        row = len(pos)
        for row_idx in range(len(pos)):
            # 兩個 Q 不可以在同一個 col 上
            if pos[row_idx] == col:
                return True
            # 兩個 Q 不可以在同一個對角線上
            if row_idx + pos[row_idx] == row + col:
                return True
            if row_idx - pos[row_idx] == row - col:
                return True
        return False

# lintcode 34
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        results  = []
        if n <= 0:
            return results
            
        pos = []
        self.dfs(n, results, pos)
        return len(results)
        
    def dfs(self, n, results, pos):
        if len(pos) == n:
            results.append(pos[:])
            return
        for i in range(n):
            if self.is_diagonal(pos, i):
                continue
            pos.append(i)
            self.dfs(n, results, pos)
            pos.pop()
            
    def is_diagonal(self, pos, val):
        m = len(pos)
        for row in range(m):
            if pos[row] == val:
                return True
            if row + pos[row] == m + val:
                return True
            if row - pos[row] == m - val:
                return True
        return False
