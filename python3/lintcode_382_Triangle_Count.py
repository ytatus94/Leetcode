# lintcode 382
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S = sorted(S)
        res = 0
        for i in range(len(S)):
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
                    
        return res
