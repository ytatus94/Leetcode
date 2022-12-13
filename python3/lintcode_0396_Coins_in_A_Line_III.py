#
#
#
#
#
# TC = O(N^2), SC = O(N^2)

# 這一題鎖住了，Leetcode 上也找不到類似的
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
