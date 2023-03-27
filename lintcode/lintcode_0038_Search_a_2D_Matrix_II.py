from typing import (
    List,
)

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        # write your code here
        n_rows = len(matrix)
        if n_rows == 0:
            return 0

        n_cols = len(matrix[0])
        if n_cols == 0:
            return 0

        count = 0
        row = 0
        col = 0
        while row < n_rows and col < n_cols:
            if matrix[row][col] == target:
                count += 1
                row += 1 # 因為數不會重複，如果有找到那就直接看下一個 
                col = 0
            elif matrix[row][col] < target:
                col += 1 # 如果比 target 小就對 col +1，當加到底的時候就要對 row +1 並把 col 歸 0
                if col == n_cols:
                    row += 1
                    col = 0
            else: # 如果比 target 大就看下一個 row 的
                row += 1
                col = 0
        return count
