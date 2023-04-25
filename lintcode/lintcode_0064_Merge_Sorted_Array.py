class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        tail_a = len(A) - 1
        ptr_a = m - 1
        ptr_b = n - 1

        while ptr_a >= 0 and ptr_b >= 0:
            if A[ptr_a] < B[ptr_b]:
                A[tail_a] = B[ptr_b]
                ptr_b -= 1
            else:
                A[tail_a] = A[ptr_a]
                ptr_a -= 1
            tail_a -= 1

        while ptr_a >= 0:
            A[tail_a] = A[ptr_a]
            tail_a -= 1
            ptr_a -= 1

        while ptr_b >= 0:
            A[tail_a] = B[ptr_b]
            tail_a -= 1
            ptr_b -= 1
