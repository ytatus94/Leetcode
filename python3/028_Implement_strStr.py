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

# 方法 2:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: # 也可以用 if needle == "" 但是執行起來會比較慢
            return 0

        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
    
    
# lintcode 13
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source is None or target is None:
            return 0
            
        if target not in source:
            return -1
        else:
            return source.index(target)
