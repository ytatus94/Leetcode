from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        for i in range(1, len(a)-1):
            if a[i] > a[i-1] and a[i] > a[i+1]:
                return i
