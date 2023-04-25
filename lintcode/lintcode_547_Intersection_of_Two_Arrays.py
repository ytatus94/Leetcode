from typing import (
    List,
)

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # write your code here
        if not nums1 or not nums2:
            return []

        hash_set = set()
        for i in nums1:
            hash_set.add(i)

        result = set()
        for i in nums2:
            if i in hash_set:
                result.add(i)

        return list(result)
