# 雙序列型 DP, 最值型 DP
# 轉移方程
#   f[i][j] = min{f[i][j-1]+1, f[i-1][j-1]+1, f[i-1][j]+1, f[i-1][j-1]|A[i-1]=B[j-1]}
#   f[i][j] 表示 A 的前 i 個字元變成 B 的前 j 個字元最少需要幾步
# 初始條件
#   f[0][j] = j, f[i][0] = i
#   空字串和長度 L 的字串，最少需要 L 步變化
# TC = O(MN), SC = O(MN) 可以用滾動數組優化成 O(N)

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps
    """
    def min_distance(self, word1: str, word2: str) -> int:
        # write your code here
        m = len(word1)
        n = len(word2)

        # f[i][j] = word1 的前 i 個元素換成 word2 的前 j 個元素最少需要幾步
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # initial condition
        # word1 是空串和 word2 是非空串 f[0][j] = j
        # word1 是非空串和 word2 是空串 f[i][0] = i

        # 看 word1 和 word2 的最後一個元素
        # case1. word1[m-1] = word2[n-1] 就看 word[0:m-1] 和 word2[0:n-1]
        # --> f[i][j] = f[i-1][j-1]
        # case2. word1[m-1] != word2[n-1]
        # 如果在 word1[m-1] 後面插入一個字元會變成 word2[n-1] 相當於看 word1[0:m] 和 word2[0:n-2]
        # --> f[i][j] = f[i][j-1]+1
        # case3. word1[m-1] != word2[n-1]
        # 如果是刪除 word1[m-1] 後剩下的 word1[m-2] = word2[n-1] 相當於看 word1[0:m-1] 和 word[0:n]
        # --> f[i][j] = f[i-1][j]+1
        # case4. word1[m-1] != word2[n-1]
        # 如果是取代 word1[m-1] 後變成 word2[n-1] 相當於看 word1[0:m-1] 和 word2[0:n-1]
        # --> f[i][j] = f[i-1][j-1]+1
        # 歸納出來最小的
        # f[i][j] = min(f[i-1][j-1]|最後的字元相等, f[i][j-1] + 1, f[i-1][j] + 1, f[i-1][j-1] + 1)
        for i in range(m + 1):
            for j in range(n + 1):
                # 這裡是初始條件
                if i == 0 or j == 0:
                    f[i][j] = i + j
                    continue

                f[i][j] = min(f[i][j - 1] + 1, f[i - 1][j] + 1, f[i - 1][j - 1] + 1)
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                    

        return f[m][n]
