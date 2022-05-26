class Solution:
    def searchBigSortedArray(self, reader, target):
        index = 1
        while reader[index - 1] < target:
            index = index * 2
            
        start = 0
        end = index - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader[mid] < target:
                start = mid
            else:
                end = mid
        if reader[start] == target:
            return start
        if reader[end] == target:
            return end
        return -1

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start, end = 0, 1
        while reader.get(end) <= target:
            end = end * 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) >= target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
