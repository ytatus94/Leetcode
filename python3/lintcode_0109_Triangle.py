# 這一題可以有許多解法，但是有的會超時
# 真正最好的解法是用 DP
# DFS Traversal (超時): TC = O(2^n)
# DFS Divid Conquer (超時): 
# Divide Conquer + Memorization
# Dynamic Programing 由上往下，但是這一題不適合用由上往下，程式碼沒由下往上好懂
# Dynamic Programing 由下往上

# 方法1. traversal (超時)
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        self.min_path_sum = float('inf')
        nrows = len(triangle)
        # 每一個 row 的 col 數目和 row 數相同
        # 例如: 第一個 row 有一個 col，第四個 row 有四個 col
        self.traversal(nrows, 0, 0, triangle, 0)
        return self.min_path_sum

    # 定義: 
    def traversal(self, nrows, row, col, triangle, path_sum):
        # 出口
        if row == nrows:
            if path_sum < self.min_path_sum:
                self.min_path_sum = path_sum
            return
        # 拆解
        new_path_sum = path_sum + triangle[row][col]
        self.traversal(nrows, row+1, col, triangle, new_path_sum)
        self.traversal(nrows, row+1, col+1, triangle, new_path_sum)
        
# 方法2. Divide Conquer (超時)
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        nrows = len(triangle)
        return self.divide_conquer(nrows, triangle, 0, 0)

    # 定義: 傳回以 triangle[row][col] 為起點的最小 path sum
    def divide_conquer(self, nrows, triangle, row, col):
        # 出口
        if row == nrows:
            return 0
        # 拆解
        path_sum1 = self.divide_conquer(nrows, triangle, row+1, col)
        path_sum2 = self.divide_conquer(nrows, triangle, row+1, col+1)
        return triangle[row][col] + min(path_sum1, path_sum2)
      
# 方法3. Divide Conquer + Memorization (這個沒超時，提交會過)
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        nrows = len(triangle)
        # 把以 triangle[row][col] 開頭的最小路徑記錄下來
        # 這樣如果已經算過了就不用再計算，可以加速程式
        self.memory = {}
        return self.divide_conquer(nrows, triangle, 0, 0)

    # 定義: 傳回以 triangle[row][col] 開頭的最小路徑和
    def divide_conquer(self, nrows, triangle, row, col):
        # 出口:
        if row == nrows:
            return 0

        # 如果已經計算過了，就會存在 memory 中，可以直接回傳結果
        if (row, col) in self.memory.keys():
            return self.memory[(row, col)]

        # 如果還沒有計算過，才去算最小路徑和
        path_sum1 = self.divide_conquer(nrows, triangle, row+1, col)
        path_sum2 = self.divide_conquer(nrows, triangle, row+1, col+1)
        self.memory[(row, col)] = triangle[row][col] + min(path_sum1, path_sum2)

        return self.memory[(row, col)]

# 方法4. DP 由上往下
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        nrows = len(triangle)
        # 狀態 f
        f = [[None] * (i+1) for i in range(nrows)]
        # 初始化頂點與三角形的兩個邊
        f[0][0] = triangle[0][0] # 頂點
        for row in range(1, nrows):
            f[row][0] = f[row-1][0] + triangle[row][0]
            f[row][row] = f[row-1][row-1] + triangle[row][row]

        # 由上往下算每個 f
        for row in range(1, nrows):
            for col in range(1, row): # 注意上限是 row (不包含 row)，因為最右邊的點的 f 已經在初始化時得到了
                # 當 row = 1 的時候 for col in range(1, 1) 不會跑，直接跳到下一個 row 值
                f[row][col] = min(f[row-1][col], f[row-1][col-1]) + triangle[row][col]

        return min(f[nrows-1]) # 找出最後一個 row 中的最小值

# 方法5. DP 由下往上
from typing import (
    List,
)

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        nrows = len(triangle)
        # 建立空的陣列來保存結果
        # f[row][col] 表示從 (row, col) 出發走到最後一層的最小路徑和
        f = [[None] * (row+1) for row in range(nrows)]

        # 初始化最後一層
        for col in range(nrows):
            f[nrows-1][col] = triangle[nrows-1][col]

        print(f)

        # 從倒數第二層往上計算 f[row][col]
        for row in range(nrows-2, -1, -1): # 
            for col in range(row+1): # col 最大等於 row 所以上限是 row+1
                print(row, col, triangle[row][col])
                min_path_sum = min(f[row+1][col], f[row+1][col+1])
                f[row][col] = triangle[row][col] + min_path_sum

        # 傳回起點的最小路徑和
        return f[0][0]
