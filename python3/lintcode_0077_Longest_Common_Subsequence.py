# 雙序列型 DP, 最值型 DP
# 轉移方程
#
# 初始條件
#
#

class Solution:
    """
    @param a: A string
    @param b: A string
    @return: The length of longest common subsequence of A and B
    """
    def longest_common_subsequence(self, a: str, b: str) -> int:
        # write your code here
        m = len(a)
        n = len(b)
        
        # f[i][j] = a 的前 i 個元素和 b 的前 j 個元素組成的 LCS 長度
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]

        # initial condition
        # 只要 a 或 b 有一個是空字串的時候，LCS 是 0

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    f[i][j] = 0
                    continue  # 注意要有這個 continue
                # f[i - 1][j] = a 的第 i 個元素 (index=i-1) 不是 LCS 一部分，
                # 只看 a 的前 i-1 個元素和 b 的前 j 個元素
                # f[i][j - 1] = b 的第 j 個元素 (index=j-1) 不是 LCS 一部分，
                # 只看 a 的前 i 個元素和 b 的前 j-1 個元素
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

                if a[i - 1] == b[j - 1]:
                    # 如果 a 的第 i 個元素 (index=i-1) 和 b 的第 j 個元素 (index=j-1)
                    # 相同，那就是 LCS 的一部分，長度 = f[i -1][j - 1] 加 1
                    f[i][j] = max(f[i][j], f[i -1][j - 1] + 1)

        return f[m][n]

# 把順序印出來
class Solution:
    """
    @param a: A string
    @param b: A string
    @return: The length of longest common subsequence of A and B
    """
    def longest_common_subsequence(self, a: str, b: str) -> int:
        # write your code here
        m = len(a)
        n = len(b)
        
        # f[i][j] = a 的前 i 個元素和 b 的前 j 個元素組成的 LCS 長度
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]
        pi = [[None for j in range(n + 1)] for i in range(m + 1)]

        # initial condition
        # 只要 a 或 b 有一個是空字串的時候，LCS 是 0

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    f[i][j] = 0
                    continue  # 注意要有這個 continue
                # f[i - 1][j] = a 的第 i 個元素 (index=i-1) 不是 LCS 一部分，
                # 只看 a 的前 i-1 個元素和 b 的前 j 個元素
                # f[i][j - 1] = b 的第 j 個元素 (index=j-1) 不是 LCS 一部分，
                # 只看 a 的前 i 個元素和 b 的前 j-1 個元素
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

                if f[i][j] == f[i - 1][j]:
                    pi[i][j] = 0
                else:
                    pi[i][j] = 1

                if a[i - 1] == b[j - 1]:
                    # 如果 a 的第 i 個元素 (index=i-1) 和 b 的第 j 個元素 (index=j-1)
                    # 相同，那就是 LCS 的一部分，長度 = f[i -1][j - 1] 加 1
                    f[i][j] = max(f[i][j], f[i -1][j - 1] + 1)

                    if f[i][j] == f[i - 1][j - 1] + 1:
                        pi[i][j] = 2

        # 最長公共子序列長度一定是 f[m][n]
        res = [None for i in range(f[m][n])]
        i, j, p = m, n, f[m][n] - 1 # p 是從 res 的最後一個元素往前
        while i > 0 and j > 0:
            if pi[i][j] == 0:
                i -= 1
            if pi[i][j] == 1:
                j -= 1
            else:
                res[p] = a[i - 1]
                p -= 1
                i -= 1
                j -= 1

        print("Longest common subsequence is:", ''.join(res))

        return f[m][n]
