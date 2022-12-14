# 可行性 DP
# 轉移方程
#   f[i][j][k] = s1[i:i+k] 和 s2[j:j+k] 的字串是否能互換後得到
#   = (f[i][j][w] and f[i+w][j+w][k-w] 其中 w 是要砍在哪 1<=w<=k-1) 或 (f[i][j+k-w][w] and f[i+w][j][k-w])
# 初始條件
#   f[i][j][1] = True 如果 s1[i] = s2[j]
#   f[i][j][1] = False 如果 s1[i] != s2[j]
# TC = O(N^4), SC = O(N^3)

class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def is_scramble(self, s1: str, s2: str) -> bool:
        # write your code here
        if len(s1) != len(s2):
            return False
        # 只有兩個字串長度相等的時候，才可能是由另一者轉換過來
        m = len(s1)
        n = len(s2)

        # 要切成子字串時需要知道 (起點, 終點) 或是 (起點, 長度)
        # f[i][j][k] = s1 起點 i 長度 k 的字串 s1[i:i+k] 能不能
        # 變成 s2 起點 j 長度 k 的字串 s2[j:j+k]
        # Built an array with size=n*n*(n+1)
        f = [[[False for k in range(n + 1)] for j in range(n)] for i in range(n)]

        # length = 1 時，單個字元
        for i in range(n):
            for j in range(n):
                f[i][j][1] = s1[i] == s2[j]

        # 看 s1 和 s2 的子字串 length = 2 開始到 n
        for length in range(2, n + 1):
            # 注意上限不可以使 i + length 超界 (i + length <= n+1)
            # i 是 s1 中子字串的起點
            for i in range(0, n - length + 1):
                # j 是 s2 中子字串的起點
                for j in range(0, n - length + 1):
                    # k 是看要切在哪裡分成 a b 兩段
                    # k 就是切完之後 a 段的長度 (b 段的長度是 length-k)
                    for k in range(1, length):
                        # s1a 變成 s2a     s1b 變成 s2b
                        if f[i][j][k] and f[i + k][j + k][length - k]:
                            f[i][j][length] = True
                            break
                    for k in range(1, length):
                        # 子字串長 length, a 段長 k, b 段長 length-k
                        # 所以 s1a (起點, 長度)=(i, k), s1b (起點, 長度)=(i+k, length-k)
                        # 所以 s2a (起點, 長度)=(j, length-k), s2b (起點, 長度)=(j+length-k, k)
                        # b 段的起點 = a 段的起點+長度
                        # s1a 變成 s2b                  s1b 變成 s2a
                        if f[i][j + length - k][k] and f[i + k][j][length - k]:
                            f[i][j][length] = True
                            break

        return f[0][0][n] # 整個 s1 和整個 s2 是否能互換
