class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        res = int(str(abs(n))[::-1])
        # 32-bin integer: -(2*32/2) to +(2**32/2) - 1
        pos_limit = (2**32 / 2) - 1
        neg_limit = -1 * (2**32 / 2)
        if res > pos_limit or res < neg_limit:
            return 0
        return res if n > 0 else -1 * res

