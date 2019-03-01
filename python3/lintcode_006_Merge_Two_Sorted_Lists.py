# lintcode 006
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        ptr_a = 0
        ptr_b = 0
        new_list = []
        while ptr_a < len(A) and ptr_b < len(B):
            if A[ptr_a] < B[ptr_b]:
                new_list.append(A[ptr_a])
                ptr_a += 1
            else:
                new_list.append(B[ptr_b])
                ptr_b += 1
        
        while ptr_a < len(A):
            new_list.append(A[ptr_a])
            ptr_a += 1
            
        while ptr_b < len(B):
            new_list.append(B[ptr_b])
            ptr_b += 1
            
        return new_list
