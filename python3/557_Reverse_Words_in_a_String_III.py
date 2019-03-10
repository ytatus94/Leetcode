class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ') # 把字串拆成單字放到 list 裡面
        
        reversed_words = []
        for word in words:
            word = word[::-1] # 把每個單字的字元反轉
            reversed_words.append(word)
            
        return ' '.join(reversed_words) # 最後要把每個單字用空白接在一起變成字串

class Solution:
    def reverseWords(self, s):
        # 把上面的步驟，用一行解決
        return ' '.join([word[::-1] for word in s.split(' ')])
