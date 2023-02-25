# 位操作型 DP, 計數型 DP
# 轉移方程:
#   f[i] = f[i>>1] + (i%2)
#   f[i] = i 的二進制表示中有多少個 1
#   f[i>>1] = i 的二進制表示右移 1 位後有多少個 1
#   i%2 = i 的二進制表示中的最後一位
# 初始條件:
#   f[0] = 0
# TC = O(N), SC = O(N)

class Solution:
    def countBits(self, n: int) -> List[int]:
        # f[i] 表示數字 i 的二進位有多少個 1
        f = [0 for i in range(n+1)]
        # 初始化
        f[0] = 0 # 數字 0 有 0 個 1

        # i%2 表示數字 i 變成二進制後最後的數是不是 1
        # i >> 1 就是二進制的右移，相當於把 i 變成 floor(i/2)
        for i in range(1, n+1):
            f[i] = (i % 2) + f[i >> 1]

        return f

# i % 2 和 i & 1 會得到相同的結果，而且 i & 1 會比較快
# i 的二進制最後一位是 1 時 i & 1 會是 1
# i 的二進制最後一位是 0 時 i & 1 會是 0
   
# 方法2:
# 找規律，會發現
# * 當 num 是偶數時，"有幾個 1" 會和 n//2 一樣
# * 當 num 是奇數時，"有幾個 1" 會比 n//2 的數目還多一個
# num  binary   有幾個1
# 0    0        0
# 1    1        1
# 2    10       1
# 3    11       2
# 4    100      1
# 5    101      2
# 6    110      2
# 7    111      3
# 8    1000     1
# 9    1001     2
# 10   1010     2
# 11   1011     3
# 12   1100     2
# 13   1101     3
# 14   1110     3
# 15   1111     4
# 16   10000    1
# 17   10001    2
# 18   10010    2
# 19   10011    3
# 20   10100    2
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                ans[i] = 0
            elif i == 1:
                ans[i] = 1
            else:
                if i % 2 == 0:
                    ans[i] = ans[i // 2]
                else:
                    ans[i] = ans[i // 2] + 1
        return ans
