class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            elif not isBadVersion(mid):
                start = mid
        
        if isBadVersion(start):
            return start
        return end
