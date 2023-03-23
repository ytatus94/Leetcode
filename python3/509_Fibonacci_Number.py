class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = [0, 1]
        sum = 0
        if N == 0:
            return temp[0]
        elif N == 1:
            return temp[1]
        elif N > 1:
            for i in range(2, N + 1):
                sum = temp[0] + temp[1]
                temp[0] = temp[1]
                temp[1] = sum
        return sum

# 方法 2
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n: int) -> int:
        # write your code here
        f = [None for i in range(n + 1)]
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n - 1] # because n counts from 1 and i count from 0
