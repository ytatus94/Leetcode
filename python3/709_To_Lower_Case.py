class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # 用內建的 lower()
        return str.lower()

class Solution:
    def toLowerCase(self, str):    
        # 自己寫
        upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        lower = list('abcdefghijklmnopqrstuvwxyz')
        upper_to_lower = dict(zip(upper,lower))
        
        lower_case = ''
        
        for char in str:
            if upper_to_lower.get(char) != None:
                lower_case = lower_case + upper_to_lower.get(char)
            else:
                lower_case = lower_case + char
                
        return lower_case

class Solution:
    def toLowerCase(self, str):
        # 用 ASCII
        # A: 65, a: 97 兩者相差 32
        return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in str])
