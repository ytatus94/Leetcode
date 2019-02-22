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

# lintcode 74
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid) == True:
                end = mid
            elif SVNRepo.isBadVersion(mid) == False:
                start = mid
                
        if SVNRepo.isBadVersion(start) == True:
            return start
        return end
