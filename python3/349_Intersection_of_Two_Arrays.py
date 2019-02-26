class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        s1 = set(nums1)
        s2 = set(nums2)
        for i in s1:
            if i in s2:
                result.append(i)
        return result

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            
        return res

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return None
        
        hash_set = set()
        
        nums1 = sorted(nums1)
        
        for i in nums2:
            if i in hash_set:
                continue
            if self.binary_search(nums1, i):
                hash_set.add(i)
                
        return list(hash_set)
    
    def binary_search(self, nums, target):
        if nums is None or len(nums) == 0:
            return False
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False

# lintcode 547
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    # 用 hash set
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
        
        hash_set = set()
        for i in nums1:
            hash_set.add(i)
            
        result = set() # 用 set() 才不會有重複的，用 list() 的話，還要比較元素有沒有重複，但是就變成 O(n^2) 會超時
        for i in nums2:
            if i in hash_set:
                result.add(i)
        
        return list(result) # 記得變成 list 的型態

class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return [i for i in s1 if i in s2]

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
