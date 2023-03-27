class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        # write your code here
        ch = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and s[i] not in ch:
                i += 1
            while i < j and s[j] not in ch:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
