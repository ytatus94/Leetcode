class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        res = []
        for i in A:
            if i != elem:
                res.append(i)
        for i in range(len(res)):
            A[i] = res[i]
        return len(res)
            
