# 序列型 DP, 最值型 DP
# 轉移方程
#   f[i][j] = min_{j-target<=k<=j+target, 1<=k<=100} (f[i-1][k] + |j-A[i-1]|)
# 初始條件
# f[1][j] = |j-A[0]| 前 1 個元素可以改成任意數值 j (1<=j<=100)，因為沒由前面相鄰的元素
# TC = (100^2 N), SC = O(100N) 可以用滾動數組優化至 O(100)

# 這題 lintcode 鎖住了，不知道寫得對不對
class Solution:
    def MinAdjustmentCost(A: list, target: int) --> int:
        n = len(A)
        if n == 0:
            return 0
          
        # f[i][j] = 把 A 的前 i 個元素改成 B 的最小代價，並且 A[i-1] 會被改成 B[i-1]=j
        # 且在 B 中的前 i 個元素，兩兩相臨的元素差不超過 target
        # 如果 A[i-1] 改成 j 那麼 A[i-2] 就只能改成 k 且 j-target<=k<=j+target
        f = [[float('-inf') for j in range(101)] for i in range(n + 1)]
        
        # initial conditions
        for i in range(1, 101):
            f[1][i] = abs(A[0] - i)
          
        for i in range(2, n + 1):
            # A[i-1] 變成 B[i-1]=j
            for j in range(1, 101):
                # A[i-2] 變成 B[i-2]=k
                for k in range(j - target, j + target + 1):
                    if k < 1 or k > 100: # k 也必須在 1 和 100 之間
                        continue
                        
                    f[i][j] = min(f[i][j], f[i - 1][k])
                    
                f[i][j] += abs(j - A[i - 1]) # 要加上修改最後一個元素的代價
                
        return min(f[n][i])
