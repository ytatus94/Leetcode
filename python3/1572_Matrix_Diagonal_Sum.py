class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # square matrix 所以 row 和 col 數目一樣
        n_rows = len(mat) # n_rows = n_cols
        result = 0
        for row in range(n_rows):
            if row != (n_rows - 1) - row: # 最後一個 col 的編號是 n_rows - 1
                result += (mat[row][row] + mat[row][(n_rows - 1) - row])
            else:
                result += mat[row][row]
        return result
