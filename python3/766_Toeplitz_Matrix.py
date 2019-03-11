class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 只比較兩個數，每個數和右下角那個數來比較 (如果右下角的數存在的話)
        # 只要不相同，那就不是 toeplitz，所以直接 retrun False
        for r in range(rows):
            for c in range(cols):
                if r + 1 <= rows - 1 and c + 1 <= cols - 1: # 如果右下角的數存在的話
                    if matrix[r][c] != matrix[r + 1][c + 1]:
                        return False
        # 能活著離開迴圈表示 diagonal 的元素都相同
        return True
