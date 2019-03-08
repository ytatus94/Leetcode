class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in A])
        
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for i in A:
            res.append(i * i)
        return sorted(res)
