from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        # write your code here
        if a is None or len(a) == 0:
            return -1

        for idx, value in enumerate(a):
            if value == target:
                return idx
        return -1
