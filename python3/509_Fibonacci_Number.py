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
