# lintcode 109
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    # 用 DFS traverse (會超時)
    def minimumTotal(self, triangle):
        # write your code here
        self.min_path = sys.maxsize
        self.traverse(triangle, 0, 0, 0)
        return self.min_path
        
    def traverse(self, triangle, x, y, sum):
        # 出口
        if x == len(triangle):
            # 打擂台
            self.min_path = min(self.min_path, sum)
            return
        
        self.traverse(triangle, x + 1, y, sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1, sum + triangle[x][y])

class Solution:
    # 用 DFS divide conquer (會超時)
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0)
        
    def divide_conquer(self, triangle, x, y):
        if x == len(triangle):
            return 0
            
        left = self.divide_conquer(triangle, x + 1, y)
        right = self.divide_conquer(triangle, x + 1, y + 1)
        return triangle[x][y] + min(left, right)

class Solution:
    # 用 DFS divide conquer + memorization
    def minimumTotal(self, triangle):
        self.hash = {}
        return self.divide_conquer_memo(triangle, 0, 0)
        
    def divide_conquer_memo(self, triangle, x, y):
        if x == len(triangle):
            return 0
            
        # 把算過的記下來，存到 hash map 裡面
        # 等到下次要用到時，先去 hash map 裡面找
        # 如果有找到，就不用重新計算，可以節省時間
        if (x, y) in self.hash:
            return self.hash[(x, y)]
            
        left = self.divide_conquer_memo(triangle, x + 1, y)
        right = self.divide_conquer_memo(triangle, x + 1, y + 1)
        self.hash[(x, y)] = triangle[x][y] + min(left, right)
        
        return self.hash[(x, y)]

class Solution:  
    # 用 DP top-down
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return -1
        if triangle[0] is None or len(triangle[0]) == 0:
            return -1
            
        # status: f[x][y] = 從 (0, 0) 到 (x, y) 的最小路徑和
        n = len(triangle)
        f = [[None for i in range(n)] for j in range(n)]
        
        # initialize
        f[0][0] = triangle[0][0]
        # 初始化三角形的最左邊和最右邊
        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
            
        # top-down 算出每一個點的最短路徑和
        # 當 i = 0 或是 j = i 時正好是三角形的最左邊和最右邊，所以要排除掉
        for i in range(1, n):
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
                
        # answer: 看最後一層的最短路徑和哪一個最小
        best = f[n - 1][0]
        for i in range(1, n):
            best = min(best, f[n - 1][i])
            
        return best

class Solution:
    # 用 DP bottom-up
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return -1
        if triangle[0] is None or len(triangle[0]) == 0:
            return -1
            
        # status: f[x][y] = 從 (0, 0) 到 (x, y) 的最小路徑和
        n = len(triangle)
        f = [[None for i in range(n)] for j in range(n)]
    
        # initialize
        # 初始化三角形的最底層
        for i in range(n):
            f[n - 1][i] = triangle[n - 1][i]

        # bottom-up
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
                
        return f[0][0]
