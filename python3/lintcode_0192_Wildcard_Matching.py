# 雙序列型 DP, 可行性 DP
# 轉移方程
#   f[i][j] = f[i-1][j-1] 如果 B[j-1]=? 或是 A[i-1]=B[j-1] 時
#   f[i][j] = f[i-1][j] 當 B[j-1]=* 且不用來匹配 or f[i][j-1] 當 B[j-1]=* 且有用來匹配
#   f[i][j] = A 的前 i 個字元能不能和 B 的前 j 個字元匹配
# 初始條件
#   f[0][0] = True 空字串和空的 wildcard 匹配
#   f[i>0][0] = False 非空的字串和空的 wildcard 不匹配
#   f[0][j>0] 可以匹配，用 f[i][j-1]
# TC = O(MN), SC = O(MN) 可以用滾動數組優化成 O(N)

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        # write your code here
        m = len(s)
        n = len(p)

        # f[i][j] = s 的前 i 個字元能不能與 p 的前 j 個字元匹配
        f = [[False for j in range(n + 1)] for i in range(m + 1)]

        # initial condition
        # f[0][0] = True # 空字串與空 wildcard 可以匹配
        # f[i>0][0] = False # 非空的字串與空的 wildcard 不能匹配
        # f[0][j>0] 是可能可以匹配的

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True # 初始條件
                    continue

                if j == 0: # 這邊必是 i > 0
                    f[i][j] = False # 初始條件
                    continue

                # 這邊必是 j > 0，但是可能 i = 0
                if p[j - 1] != '*':
                    # case1 p[j-1]=s[i-1]
                    # case2 p[j-1]=? 必可以匹配 s[i-1]
                    # 這兩種情況都看 s[0:i-1] 和 p[0:i-1] 能否匹配
                    if (i > 0 and # 要注意 i > 0
                       (s[i - 1] == p[j - 1] or p[j - 1] == '?') 
                    ):
                        f[i][j] |= f[i - 1][j - 1]
                else: 
                    # 當 p[j-1]=* 時可以匹配 s 的 0 個或一個以上的字元
                    # case3 p[j-1]=* 匹配 s 的 0 個字元
                    f[i][j] |= f[i][j - 1]
                    # case4 p[j-1]=* 匹配 s 的一個以上的字元時，把 s 的最後一個字元刪掉
                    # 檢查 p 是否與 s[0:i-1] 匹配
                    if i > 0:
                        f[i][j] |= f[i - 1][j]

        return f[m][n]
                    
# 印出來匹配的字元
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        # write your code here
        m = len(s)
        n = len(p)

        # f[i][j] = s 的前 i 個字元能不能與 p 的前 j 個字元匹配
        f = [[False for j in range(n + 1)] for i in range(m + 1)]

        pi = [[False for j in range(n + 1)] for i in range(m + 1)]

        # initial condition
        # f[0][0] = True # 空字串與空 wildcard 可以匹配
        # f[i>0][0] = False # 非空的字串與空的 wildcard 不能匹配
        # f[0][j>0] 是可能可以匹配的

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True # 初始條件
                    continue

                if j == 0: # 這邊必是 i > 0
                    f[i][j] = False # 初始條件
                    continue

                # 這邊必是 j > 0，但是可能 i = 0
                if p[j - 1] != '*':
                    # case1 p[j-1]=s[i-1]
                    # case2 p[j-1]=? 必可以匹配 s[i-1]
                    # 這兩種情況都看 s[0:i-1] 和 p[0:i-1] 能否匹配
                    if (i > 0 and # 要注意 i > 0
                       (s[i - 1] == p[j - 1] or p[j - 1] == '?') 
                    ):
                        pi[i][j] = 1 # 刪掉 s 和 p 的最後一個字元
                        f[i][j] |= f[i - 1][j - 1]
                else: 
                    # 當 p[j-1]=* 時可以匹配 s 的 0 個或一個以上的字元
                    # case3 p[j-1]=* 匹配 s 的 0 個字元
                    f[i][j] |= f[i][j - 1]
                    if f[i][j - 1] == True:
                        pi[i][j] = 2 # 刪掉 p 末尾的 *
                    # case4 p[j-1]=* 匹配 s 的一個以上的字元時，把 s 的最後一個字元刪掉
                    # 檢查 p 是否與 s[0:i-1] 匹配
                    if i > 0:
                        f[i][j] |= f[i - 1][j]
                        if f[i - 1][j] == True:
                            pi[i][j] = 3 # p 末尾的 * 匹配 s 末尾的字元

        if f[m][n]:
            res = [None for i in range(m + 1)]
            # res[i] 表示 s[i] 會和 p[res[i]] 匹配
            i, j = m, n
            while True:
                if j == 0:
                    break
                if pi[i][j] == 1:
                    res[i-1] = j - 1
                    i -= 1
                    j -= 1
                elif pi[i][j] == 2:
                    j -= 1
                elif pi[i][j] == 3:
                    res[i - 1] = j - 1
                    i -= 1

            for i in range(m):
                print(f'{s[i]} matches {p[res[i]]}' )

        return f[m][n]
