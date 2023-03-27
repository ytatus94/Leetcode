class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s: str, p: str) -> bool:
        # write your code here
        m = len(s)
        n = len(p)

        # f[i][j] = s 的前 i 個字元是否能與 p 的前 j 個字元匹配
        f = [[False for j in range(n + 1)] for i in range(m + 1)]
        
        # initial conditions
        # f[0][0] = True # 空字串和空的 RE 能匹配
        # f[i>0][0] = False # 非空的字串和空的 RE 不能匹配
        # f[0][j] 空的字串和非空的 RE 是屬於 的情形，可以匹配的

        # case1. p 的最後一個字元和 s 的最後一個字元 相同
        # s[i-1]=p[j-1] 匹配，要看 s[0:i-1] 和 p[0:j-1] 能否匹配
        # case2. p 的最後一個字元是 . 必能匹配 s 的最後一個字元
        # 要看 s[0:i-1] 和 p[0:j-1] 能否匹配
        # 所以 case1 和 case2 是用相同的轉移方程
        # case3. p 的最後一個字元是 * 要看 p 的倒數第二個字元 p[j-2]
        # s[i-1]!=p[j-2] 時，表示 p[j-2:j] 的字元在 s 中出現 0 次，可以直接忽略
        # 只看 s[0:i] 和 p[0:j-2] 能否匹配
        # case4. p 的最後一個字元是 * 要看 p 的倒數第二個字元 p[j-2]
        # s[i-1]=p[j-2] 或 p[j-2]= . 時，s[i-1] 之前的字元仍然有可能與 p[j-2] 匹配，所以
        # 看 s[0:i-i] 和 p 能否匹配

        for i in range(m + 1):
            for j in range(n + 1):
                # initial conditions
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue # 要記得 continue

                # 會到這裡表示 i != 0
                if j == 0:
                    f[i][j] = False
                    continue # 要記得 continue

                # 會到這裡表示 j > 0 (但是有可能 i = 0)
                if p[j - 1] != '*':
                    # case1 && case 2
                    if (i > 0 and # 要注意加上 i > 0 因為要用到 i-1
                       (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                    ):
                        f[i][j] = f[i - 1][j - 1]
                    else:
                        # case3
                        if j > 1: # 注意要 j > 1 因為要用到 j-2
                            f[i][j] |= f[i][j - 2]
                        # case4
                        if i > 0 and j > 1: # 因為要用到 i-1 和 j-2
                            if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                                f[i][j] |= f[i - 1][j]
        return f[m][n]
