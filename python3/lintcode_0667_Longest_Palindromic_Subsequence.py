# 區間型 DP
# 轉移方程
# f[i][j] = max( f[i+1][j], f[i][j-1], f[i+1][j-1]+2|s[i]=s[j] )
#         = i...j 之間最長的回問子字串的長度
# 初始條件
# f[0][0] = f[1][1] = ... = f[n-1][n-1] = 1 一個字元也是回文子字串
# s[i] = s[i+1] 時 f[i][i+1] = 2
# s[i] != s[i+1] 時 f[i][i+1] = 1
# TC = O(N^2), SC = O(N^2)

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longest_palindrome_subseq(self, s: str) -> int:
        # write your code here
        n = len(s)
        if n == 0:
            return 0

        # f[i][j] = 從 i 到 j 的最長回文子字串的長度
        # 如果 s[i] = s[j] 那回文子字串一定在 i...j 之間
        # 如果 s[i] != s[j] 那回文子字串一定在 i+1...j 或是 i...j-1 之間
        f = [[0 for j in range(n)] for i in range(n)]
        # initial condition
        # 長度 = 1
        for i in range(n):
            f[i][i] = 1 # 自己一個字元也算是回文串
        # 長度 = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2
            elif s[i] != s[i + 1]:
                f[i][i + 1] = 1

        # 長度 3 含以上
        for length in range(3, n + 1): # 按照長度由小到大計算
            for i in range(n - length + 1): # 最後一個允許的 i 是 n-length, 這樣 j 才不會超界
                j = i + length - 1
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i + 1][j - 1] + 2)

        return f[0][n - 1]

# 印出回文子序列
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longest_palindrome_subseq(self, s: str) -> int:
        # write your code here
        n = len(s)
        if n == 0:
            return 0

        # f[i][j] = 從 i 到 j 的最長回文子字串的長度
        # 如果 s[i] = s[j] 那回文子字串一定在 i...j 之間
        # 如果 s[i] != s[j] 那回文子字串一定在 i+1...j 或是 i...j-1 之間
        f = [[0 for j in range(n)] for i in range(n)]
        pi = [[0 for j in range(n)] for i in range(n)]
        # initial condition
        # 長度 = 1
        for i in range(n):
            f[i][i] = 1 # 自己一個字元也算是回文串
        # 長度 = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2
            elif s[i] != s[i + 1]:
                f[i][i + 1] = 1

        # 長度 3 含以上
        for length in range(3, n + 1): # 按照長度由小到大計算
            for i in range(n - length + 1): # 最後一個允許的 i 是 n-length, 這樣 j 才不會超界
                j = i + length - 1
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if f[i][j] == f[i + 1][j]: # 去頭
                    pi[i][j] = 0
                else: # f[i][j] = f[i][j - 1] 去尾
                    pi[i][j] = 1
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i + 1][j - 1] + 2)
                    if f[i][j] == f[i + 1][j - 1] + 2: # 去頭又去尾
                        pi[i][j] = 2

        # 開一個長度是 f[0][n - 1] 的字串，用 f[0][n - 1] 是因為知道這是最長回文串的長度
        res = [None for i in range(f[0][n - 1])]
        p = 0
        q = f[0][n - 1] - 1
        i = 0
        j = n - 1
        while i <= j:
            if i == j: # 長度為 1
                res[p] = i
                break
            
            if i + 1 == j: # 長度為 2
                res[p] = s[i]
                res[q] = s[j]
                break

            if pi[i][j] == 0: # 去頭的情形
                i += 1
            else:
                if pi[i][j] == 1: # 去尾的情形
                    j -= 1
                else: # 去頭又去尾
                    res[p] = s[i]
                    res[q] = s[j]
                    p += 1
                    q -= 1
                    i += 1
                    j -= 1

        print("result is", "".join(res))

        return f[0][n - 1]
