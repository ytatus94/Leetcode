class Solution:
    """
    @param A: An integer
    @return: a float number
    """
    def maxOfArray(self, A):
        # write your code here
        res = A[0]
        for i in A:
            if i > res:
                res = i
        return res
