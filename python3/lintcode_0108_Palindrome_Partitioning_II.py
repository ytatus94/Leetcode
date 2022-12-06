# 劃分型 DP, 最值型 DP
# 轉移方程:
#   f[i] = min_{0<=j<=i-1}( f[j]+1|s[j...i-1]是回文串 ) --> 這個 TC = O(N^3), 要 loop i, j 和 j...i-1 會超時
#   f[i] = min_{0<=j<=i-1}( f[j]+1|isPalin[j][i-1]=True ) --> 這個 TC = O(N^2) 快一些
#   f[i] = 前 i 個字元最 s[0...i-1] 最少可以被劃分成幾個回文串
#   注意題目要求的是 minimum cut 不是幾個回文串
#   minimum cut = f[n] - 1
# 初始條件:
#   f[0] = 0 空字串可以被劃分成 0 個回文串
# TC = O(N^2), SC = O(N^2)

class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s: str) -> int:
        # write your code here
        if s is None:
            return 0

        n = len(s)
        if n == 0:
            return 0

        isPalin = self.calcPalin(s)
        print(isPalin)

        # 開一個數組紀錄前 i 個字元最少有多少個回文串
        f = [float('inf') for i in range(n + 1)]
        # 初始條件
        f[0] = 0 # 前 0 個字元是空字串，沒有回文串
        
        for i in range(1, n + 1):
            for j in range(0, i):
                if isPalin[j][i-1]:
                    f[i] = min(f[i], f[j] + 1)

        # 植樹問題
        # 切成 f[n] 個回文串要切 f[n]-1 刀
        print(f[n])
        return f[n] - 1

    # 用一個 TC = O(N^2) 的先算出所有可能的回文串
    def calcPalin(self, s):
        n = len(s)
        f = [[False for i in range(n)] for j in range(n)]

        # n 是奇數，正中間那個是一個字元
        for c in range(n): # 枚舉所有正中間字元的位置
            i = j = c
            while i >= 0 and j < n and s[i] == s[j]:
                f[i][j] = True # 由 i 到 j 的是回文串
                i -= 1
                j += 1

        # n 是偶數，正中間那個是兩個字元間的分隔線
        for c in range(n - 1): # 枚舉所有正中間分隔線，只能到 n - 1 這樣 j 才不會出界
            i = c
            j = c + 1
            while i >= 0 and j < n and s[i] == s[j]:
                f[i][j] = True
                i -= 1
                j += 1

        return f
