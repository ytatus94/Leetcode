class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 方法一 慢
        # start = 0
        # end = len(A) - 1
        # while start + 1 < end:
        #     mid = start + (end - start) // 2
        #     if A[mid - 1] < A[mid]  and A[mid] > A[mid + 1]:
        #         return mid
        #     elif A[mid - 1] < A[mid + 1]:
        #         start = mid
        #     elif A[mid - 1] > A[mid + 1]:
        #         end = mid
        # if A[start] > A[end]:
        #     return start
        # return end
        
        # 方法二
        # 題目說明先增後減了，只要找到後一個比目前小的就是峰值
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i
