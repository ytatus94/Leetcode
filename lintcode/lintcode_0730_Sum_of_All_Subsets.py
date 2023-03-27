class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def sub_sum(self, n: int) -> int:
        # write your code here
        if n == 0:
            return 0

        sum_n_integers = 0
        for i in range(1, n+1):
            sum_n_integers += i

        results = sum_n_integers * 2**(n-1)
        return results

# 這一題是 easy 
# 理論上看到要求所有可能的集合之和，要先想到 DFS
# 但是因為是 easy 程度，可能有比 DFS 更簡單的解法
# 於是先找規律
# n = 2:
# [1], [1,2]
# [2]
# sum = 1 + 1 + 2 + 2 = 6
# 1 出現 2 次
# 2 出現 2 次
# --> (1 + 2) * 2 = (1+2)*2^1 = (1+2)*2^(2-1)= 6
#
# n = 3:
# [1], [1,2], [1,3], [1,2,3]
# [2], [2,3]
# [3]
# sum = 1 + 1+2 + 1+3 + 1+2+3 + 2 + 2+3 +3 = 24
# 1 出現 4 次
# 2 出現 4 次
# 3 出現 4 次
# --> (1+2+3) * 4 = (1+2+3+4)* 2^2 = (1+2+3+4)*2^(3-1)=24
#
# n = 4:
# 歸納出 sum = (1+2+3+4)*2^(4-1)=(1+2+3+4)*2^3 = 80

# 方法2
class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def sub_sum(self, n: int) -> int:
        # write your code here
        # return sum([i for i in range(1, n+1)]) * 2**(n-1)
        return int((1 + n) * n / 2) * 2**(n-1)
