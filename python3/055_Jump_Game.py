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

class Solution:
    # 用貪心算法
    def canJump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return False
            
        farthest = A[0] # 目前能走最遠是走到 fasthest 的位置
        for i in range(1, len(A)):
            # 如果 i <= farthest 表示能走到 i
            # 走到 i 之後，要計算從 i 開始能走最遠是走到哪
            # 然後更新最遠距離
            if i <= farthest and A[i] + i >= farthest:
                farthest = A[i] + i
                
        return farthest >= len(A) - 1
