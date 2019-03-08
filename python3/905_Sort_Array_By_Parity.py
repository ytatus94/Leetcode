class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even =[]
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
        
class Solution:
    def sortArrayByParity(self, A):
        # 看到一個別的方法
        return sorted(A, key=lambda x: x%2)
