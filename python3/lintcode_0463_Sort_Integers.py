from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        # write your code here
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

