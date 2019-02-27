class Solution:
    def searchBigSortedArray(reader, target):
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
