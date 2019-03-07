# lintcode 486
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        return self.merge_helper(arrays, 0, len(arrays) - 1)
        
    def merge_helper(self, nums, start, end):
        if start == end:
            return nums[start]
            
        mid = (start + end) // 2
        left_part = self.merge_helper(nums, start, mid)
        right_part = self.merge_helper(nums, mid + 1, end)
        return self.merged_two_sorted_array(left_part, right_part)
        
    def merged_two_sorted_array(self, nums1, nums2):
        if nums1 is None or len(nums1) == 0:
            return nums2
            
        if nums2 is None or len(nums2) == 0:
            return nums1
            
        res = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
            else:
                res.append(nums2[index2])
                index2 += 1
        if index1 < len(nums1):
            res += nums1[index1:]
        if index2 < len(nums2):
            res += nums2[index2:]
        return res

# top-down
class Solution:
    def mergekSortedArrays(self, arrays):
        if arrays is None or len(arrays) == 0:
            return []
        while len(arrays) > 1:
            merged = []
            for i in range(0, len(arrays) - 1, 2):
                merged.append(self.merge_two_sorted_arrays_1(arrays[i], arrays[i + 1]))
                # merged.append(self.merge_two_sorted_arrays_2(arrays[i], arrays[i + 1]))
            if len(arrays) % 2 == 1:
                merged.append(arrays[-1])
            arrays = merged
        return arrays

    def merge_two_sorted_arrays_1(self, nums1, nums2):
        if nums1 is None:
            return nums2
        if nums2 is None:
            return nums1
        return sorted(nums1 + nums2)

    def merge_two_sorted_arrays_2(self, nums1, nums2):
        if nums1 is None or len(nums1) == 0:
            return nums2
        if nums2 is None or len(nums2) == 0:
            return nums1
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < len(nums1):
            res += nums1[i:]
        if j < len(nums2):
            res += nums2[j:]
        return res
