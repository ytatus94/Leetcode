class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        for word in words:
            morse = ''
            for ch in word:
                # 小寫字母 a 的 ASCII 是 97
                morse += code[ord(ch) - 97]
            res.add(morse)
        
        return len(res)
        
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        char = list('abcdefghijklmnopqrstuvwxyz')
        char_to_morse_code = dict(zip(char, morse_code))
        
        words_in_morse_code = list()
        for word in words:
            convert_to_morse_code = ''
            for i in word:
                convert_to_morse_code += char_to_morse_code[i]
            words_in_morse_code.append(convert_to_morse_code)
                
        return len(set(words_in_morse_code))
