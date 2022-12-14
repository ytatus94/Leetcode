# 雙序列型 DP, 存在型 DP
# 轉移方程
#   f[i][j] = (f[i-1][j] | s3[i+j-1]==s1[i-1]) or (f[i][j-1] | s3[i+j-1]==s2[j-1])
# 初始條件
#   f[0][0] = 0 空串 s1 與空串 s2 可以組成空串 s3
# TC = O(MN), SC = O(MN) 可以用滾動數組優化成 O(N)

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        # write your code here
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        # f[i][j] = s1 的前 i 個元素和 s2 的前 j 個元素組成 s3 的前 i+j 個元素和
        # case 1: s1[i-1] = s3[i+j-1] (s1 和 s3 最後一個元素相同)
        # s3 的前 i+j-1 個元素 (s3[0:i+j-1]) 由 s1 的前 i-1 個元素 (s1[0:i-1]) 和 s2 的前 j 個元素組成
        # case 2: s2[j-1] = s3[i+j-1] (s2 和 s3 最後一個元素相同)
        # s3 的前 i+j-1 個元素 (s3[0:i+j-1]) 由 s1 的前 i 個元素和 s2 的前 j-1 個元素 (s2[0:j-1])組成
        f = [[False for j in range(n + 1)] for i in range(m + 1)]
        
        # initial condition
        # s1 的前 0 個元素和 s2 的前 0 個元素能組成 s3 的前 0 個元素
        # 就是說空字串和空字串能組成空字串
        # f[0][0] = True
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                # 如果 s3 的最後一個元素 s3[i+j-1]是 s1 的最後一個元素 s1[i-1]
                # 那 s3[0: i+j-2] 是由 s1[0:i-1] 和 s2 組成
                if i > 0 and s3[i + j - 1] == s1[i - 1]:
                    f[i][j] |= f[i - 1][j]
                # 如果 s3 的最後一個元素 s3[i+j-1]是 s2 的最後一個元素 s2[j-1]
                # 那 s3[0: i+j-2] 是由 s1 和 s2[0:j-2] 組成
                if j > 0 and s3[i + j - 1] == s2[j - 1]:
                    f[i][j] |= f[i][j - 1]
        
        return f[m][n]
