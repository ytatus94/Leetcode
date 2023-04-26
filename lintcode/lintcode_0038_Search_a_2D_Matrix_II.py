# 方法 1 超時了
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

# 方法 2: 這個才會過
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
        if matrix is None or len(matrix[0]) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # 每一個 row 的數字都是排序好的，而且沒有重複的數字
        # 比對每個 row 最後一個值，如果比 target 小，就直接看下一 row
        # 如果在該 row 有找到 target 也直接看下一個 row
        count = 0
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] < target: # 這個 row 不會有 target 了
                row += 1
            elif matrix[row][col] > target: # 這個 row 可能有 target
                col -= 1
            elif matrix[row][col] == target: # 找到了就直接看下一個 row
                count += 1
                row += 1
                col = cols - 1

        return count
