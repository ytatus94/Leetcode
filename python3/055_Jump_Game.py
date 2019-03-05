# lintcode 116
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return False
            
        # status
        f = [False for i in range(len(A))]
        # initialize
        f[0] = True
        # function
        # 要看能不能走到第 i 個元素的位置
        # 所以要看比 i 小的元素 j
        # 首先要能走到 j 的位置，然後 j 的位置上允許移動的步伐數目要 > i
        for i in range(1, len(A)):
            for j in range(i):
                if f[j] and j + A[j] >= i:
                    f[i] = True
                    
        return f[len(A) - 1]
