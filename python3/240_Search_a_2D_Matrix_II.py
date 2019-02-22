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

# lintcode 38
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        nrows = len(matrix)
        if nrows == 0:
            return 0
            
        ncols = len(matrix[0])
        if ncols == 0:
            return 0
            
        count = 0
        row = 0
        col = 0
        while row < nrows and col < ncols:
            if matrix[row][col] == target:
                print(row, col)
                count += 1
                row += 1
                col = 0
                
            elif matrix[row][col] < target:
                col += 1
                if col == ncols:
                    row += 1
                    col = 0
            else:
                row += 1
                col = 0

        return count
