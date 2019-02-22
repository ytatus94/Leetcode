class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 因為每一個 row 的第一個數，一定比上一個 row 的第一個數還大
        # 所以先找垂直方向的，確定 target 落在哪一個 row
        # 再找水平方向的
        
        if not matrix: # 空的
            return False
        
        # 方法ㄧ 48 ms beat 42.54%
        for row in matrix:
            if target in row:
                return True
        return False
    
        # 方法二
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0: # matrix = []
            return False
        if cols == 0: # matrix = [[]]
            return False
        
        start = 0
        end = rows - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            print(matrix[mid][0])
            if matrix[mid][0] == target:
                return True # target 剛好是某 row 的第一個數
            elif matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] > target:
                end = mid
        # 離開迴圈時，target 的值一定在 start 或 end 所在的 row 的範圍裡
        # 所以要先判斷是在 start 的那一個 row 或 end 的那一個 row
        target_row = 0
        if matrix[end][0] > target: # target 會在 start 的那一個 row
            target_row = start
        else: # target 會在 end 的那一個 row
            target_row = end
        
        # 會跑到這邊表示 target 在 row 的範圍裡，但是還不確定 target 是否存在
        # 所以要去判斷 target 是否在該 row 裡面
        head = 0
        tail = len(matrix[target_row]) - 1

        while head + 1 < tail:
            mid = head + (tail - head) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                head = mid
            elif matrix[target_row][mid] > target:
                tail = mid
        print(head, tail)
        # 離開迴圈時，要麻 target 是 head，要麻 target 是 tail，否則就是不存在
        if matrix[target_row][head] == target or matrix[target_row][tail] == target:
            return True
        return False
