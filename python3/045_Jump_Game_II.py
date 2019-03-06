# lintcode 117
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    # 用 DP 會超時
    def jump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        # status    
        step = [sys.maxsize for i in range(len(A))]
        # initialize
        step[0] = 0
        # function
        # 要移動到元素 i 的畫，就必須是在 i 前面的某個元素 j 上
        # 然後在 j 的允許步伐內可以跳到 i
        for i in range(1, len(A)):
            for j in range(i):
                if step[j] != sys.maxsize and A[j] + j >= i:
                    step[i] = min(step[i], step[j] + 1)
        # answer
        return step[len(A) - 1]

class Solution:
    # 用貪心算法
    def jump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1
            
        start, end, steps = 0, 0, 0
        while end < len(A) - 1:
            steps += 1
            farthest = end
            for i in range(start, end+1):
                if A[i] + i > farthest:
                    farthest = A[i] + i
            start = end + 1
            end = farthest
            
        return steps
