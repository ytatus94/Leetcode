class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        '''
        畫圖觀察可以得知
        xy 平面上看，就是 grid 有幾個非零的元素個數
        xz 平面上看，就是每一個 col 的最大值的和
        yz 平面上看，就是每一個 row 的最大值的和       
        '''
        xy, xz, yz = 0, 0, 0
        
        for row in grid:
            for col in row:
                if col != 0:
                    xy += 1
                    
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            xz += max(column)
                
        for row in grid:
            yz += max(row)
            
        return xy + xz + yz
        
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # 方法2: 比較慢
        # *grid 會 unpack list
        # grid = [[1,2],[3,4]] 則 *grid = [1,2],[3,4]
        xy = sum(1 for v in grid for e in v if e != 0)
        xz = sum(max(v) for v in zip(*grid)) 
        yz = sum(max(v) for v in grid)
        
        return xy + xz + yz
