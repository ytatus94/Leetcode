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

# lintcode 33
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        if n <= 0:
            return results
          
        nums = [i for i in range(n)]
        
        # 紀錄 queens 的位置，每一行每一列每一個對角線上只能有一個皇后
        # 每一個元素的 index 表示第幾個 row，每一個元素的值表示第幾個 column
        # 因為每一個元素只會放一個值，可以確保每個 row 上只有一個皇后
        # 只要每個元素的值都不同，就可以確保每個 col 上只有一個皇后
        queens_position = []
        self.dfs(nums, results, queens_position)
        # print(results)
        return results
        
    def dfs(self, nums, results, queens_position):
        if len(queens_position) == len(nums):
            # 確保每一條對角線上只有一個皇后
            # if not self.is_diagonal(queens_position):
            chase_board = self.draw_queens_position(queens_position)
            results.append(chase_board)
        for i in range(len(nums)):
            # 用過的不能再用了，這樣可以保證每一個 col 上只有一個皇后 
            if nums[i] in queens_position:
                continue
            # 確保每一條對角線上只有一個皇后
            if self.is_diagonal(queens_position, nums[i]):
                continue
            queens_position.append(nums[i])
            self.dfs(nums, results, queens_position)
            queens_position.pop()
            
    def is_diagonal(self, position, val):
        n = len(position)
        for x in range(n):
            if x + position[x] == n + val:
                return True
            if x - position[x] == n - val:
                return True
        return False
        
    def draw_queens_position(self, position):
        n = len(position)
        chase_board = []
        for queen in position:
            string = ['.' if i != queen else 'Q' for i in range(n)]
            chase_board.append(''.join(string))
        return chase_board
