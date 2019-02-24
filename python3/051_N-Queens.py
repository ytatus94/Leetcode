class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 目標是要把每一列皇后鎖允許的位置記錄下來
        # 兩個皇后不能放在同一條斜線上，不能放在同一列，不能放在同一欄
        if n <= 0:
            return [[]]
        
        results = []
        
        # 用來記錄皇后放在哪一個欄位
        # 第 i 個元素表示第 i 列，第 i 個元素的值表示放在該列的第幾欄
        cols = []
        
        self.dfs(n, results, cols)
        return results
    
    def dfs(self, n, results, cols):
        if len(cols) == n:
            results.append(self.draw_chessboard(cols))
            return
        
        row = len(cols)
        # 這邊是 loop 每一列，看每一列的皇后要放在哪一個欄位
        for col_index in range(n):
            # 如果不能放，就看下一個欄位
            if not self.is_valid(col_index, cols):
            # if not self.is_valid(cols, row, col_index):
                continue
                
            # 如果可以放，就加到 cols 裡面
            # 每一列的皇后要放在第 i 欄，每 append() 一次就是一個 row
            cols.append(col_index)
            self.dfs(n, results, cols)
            cols.pop()

    def draw_chessboard(self, cols):
        # cols 的第 i 個元素表示第 i 列，第 i 個元素的值 val 表示第 val 欄位
        n = len(cols)
        board = []
        for row in range(n): 
            value = ['Q' if column == cols[row] else '.' for column in range(n)]
            board.append(''.join(value))
        return board

    def is_valid(self, column, cols):
        # 現在是第幾個 row 可以藉由計算 cols 的長度來得到
        rows = len(cols) 
        for row_index in range(rows):
            # 同一行或是同一列只能放一個皇后
            if column == cols[row_index]:
                return False
            # 同一條斜線上也只能放一個皇后
            # 右上到左下的斜線 x + y 和相等
            if row_index + cols[row_index] == rows + column:
                return False
            # 左上到右下的斜線 x - y 差相等
            if row_index - cols[row_index] == rows - column:
                return False
            
        return True
