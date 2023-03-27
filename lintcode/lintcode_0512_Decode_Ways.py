# 劃分型 DP, 計數型 DP
# 轉移方程:
#   f[i] = f[i-1]|S[i-1] 對應一個字母 + f[i-2]|S[i-2][i-1]對應一個字母
#   f[i] = 解碼 S 的前 i 個數字成字母有多少種方式
# 初始條件:
#   f[0] = 1 空字串只有一種解碼方式
# TC = O(N), SC = O(N)

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def num_decodings(self, s: str) -> int:
        # write your code here
        if len(s) == 0:
            return 0 # 空字串要傳回 0 或 1 是看題目的定義，這題定義是 0

        # 開一個長度是 len(s)+1 的數組，並且初始化為 0
        # f[i] = 前 i 個數時有幾種解碼方式
        f = [0 for i in range(len(s) + 1)]

        # 初始化
        f[0] = 1 # "前" 0 個數只有一種解碼方式

        # a.) 只看 s[i-1] 來解碼: f[i] = f[i - 1]
        # b.) 把 s[i-2]s[i-1] 當成一個數來解碼 (這時候 10 <= s[i-2]s[i-1] <= 26): 
        # f[i] = f[i - 2]
        # 所以 f[i] = a.)的方法數 + b.)的方法數

        for i in range(1, len(s) + 1):
            # 只看 s[i-1] 來解碼
            if 1 <= int(s[i-1]) <= 9:
                f[i] += f[i - 1]

            # 看 s[i-2]s[i-1] 來解碼
            if i - 2 >= 0: # 要確保下標不會不存在
                number = int(s[i - 2: i])
                if 10 <= number <= 26:
                    f[i] += f[i - 2]
        return f[len(s)]

