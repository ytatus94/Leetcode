class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 有可能的情形是: 嚴格遞增，嚴格遞減，有增有減
        # 嚴格遞減: 第一個數是 peak
        # 嚴格遞增: 最後一個數是 peak
        # 有增有減: 找到第一個峰就可以 return 了

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]: # 上升中，峰在 mid 右邊
                start = mid
            if nums[mid] > nums[mid + 1]: # 下降中，峰在 mid 左邊
                end = mid
        # 離開迴圈時 start, end 一定一大一小
        if nums[start] > nums[end]:
            return start
        return end

# lintcode 75
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if len(A) == 0:
            return -1
            
        start = 1
        end = len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] > A[mid - 1]:
                start = mid
            elif A[mid] > A[mid + 1]:
                end = mid
            else:
                end = mid
        if A[start] > A[end]:
            return start
        return end
