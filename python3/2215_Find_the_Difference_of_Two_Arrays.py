# 方法1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_not_in_nums2 = list(set(i for i in nums1 if i not in nums2))
        num2_not_in_nums1 = list(set(i for i in nums2 if i not in nums1))
        return [num1_not_in_nums2, num2_not_in_nums1]

# 方法2
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
