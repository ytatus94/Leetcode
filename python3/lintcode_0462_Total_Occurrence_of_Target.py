from typing import (
    List,
)

class Solution:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def total_occurrence(self, a: List[int], target: int) -> int:
        # write your code here
        if a is None or len(a) == 0:
            return 0
        count = 0
        for i in a:
            if i == target:
                count += 1
        return count
