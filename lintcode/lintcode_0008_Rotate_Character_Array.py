from typing import (
    List,
)

class Solution:
    """
    @param s: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotate_string(self, s: List[str], offset: int):
        # write your code here
        if s is None or len(s) == 0:
            return
        
        double_str = s + s
        offset = offset % len(s)

        start_index = len(s) - offset
        end_index = start_index + len(s)

        new_string = double_str[start_index : end_index]

        for i in range(len(s)):
            s[i] = new_string[i]
