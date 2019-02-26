class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1) - 1
        while m - 1 >= 0 and n - 1 >= 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
            else:
                nums1[index] = nums2[n - 1]
                n -= 1
            index -= 1
            
        while m - 1 >= 0:
            nums1[index] = nums1[m - 1]
            index -= 1
            m -= 1
            
        while n - 1 >= 0:
            nums1[index] = nums2[n - 1]
            index -= 1
            n -= 1
            
# lintcode 64
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
            print(A[ptr_a], B[ptr_b])
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
