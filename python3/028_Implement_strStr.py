class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: # 空 string 要這樣判斷，不可以用 needle == None
            return 0
        if len(haystack) < len(needle):
            return -1
        
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
            
        return -1
