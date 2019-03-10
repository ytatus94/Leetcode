class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 最簡單的寫法，但是似乎很慢
        # return list(zip(*A))

class Solution:
    def transpose(self, A):
        # 兩個 for loop 都比上面的快
        rows = len(A)
        cols = len(A[0])
        
        b = []
        for i in range(cols):
            c = []
            for j in range(rows):
                c.append(A[j][i])
            b.append(c)
        return b
