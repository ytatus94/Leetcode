# 博弈型 DP, 存在型 DP
# 轉移方程
#   f[i][j] = max(a[i] - f[i+1][j], a[j] - f[i][j-1])
#   f[i][j] = 從 i 到 j 中，選 i 或選 j 使得兩方數字和有最大的差值
#   a[i] - f[i+1][j]: 選 i 了，所以另一方最大的差值是 f[i+1][j]
#   a[j] - f[i][j-1]: 選 j 了，所以另一方最大的差值是 f[i][j-1]
# 初始條件
#   f[i][i] = a[i] i 從 0 到 N-1
#   只剩下一個數字 (假設剩第 i 個) 那差值就是 a[i]
# TC = O(N^2), SC = O(N^2)

# 這一題 lintcode 鎖住了，Leetcode 上也找不到類似的
# 所以不知道答案對不對
class Solution:
    def firstWillWin(A: list) -> bool:
        n = len(A)
        f = [[0 for j in range(n + 1)] for i in range(n + 1)]
        
        for i in range(n):
            f[i][i] = A[i]
            
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                f[i][j] = max(A[i] - f[i + 1][j], A[j] - f[i][j - 1])
                
        return f[0][n - 1] >= 0
