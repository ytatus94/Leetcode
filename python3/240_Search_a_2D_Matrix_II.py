class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in matrix:
            if target in row:
                return True
        return False
