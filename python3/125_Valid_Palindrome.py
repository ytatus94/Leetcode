class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 先把 s 中的標點符號移除，只考慮字母和數字
        # 然後全部轉成小寫
        # re.sub() 把不符合 a-zA-Z0-9 的都用 '' 取代了
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        # 也可以用
        # s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]
        
# lintcode 415
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return True
        
        # 先全部轉換成小寫    
        s = s.lower()
        # 把空白和標點符號移除，只保留字母和數字
        new_string = '' # 空字串
        for i in s:
            if i.isalpha() or i.isdigit():
                new_string += i
        
        head = 0
        tail = len(new_string) - 1
        while head < tail:
            if new_string[head] != new_string[tail]:
                return False
            head += 1
            tail -= 1
        
        return True
