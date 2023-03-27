# lintcode 171
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        if strs is None:
            return None
        
        res = []
        hash = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hash:
                hash[sorted_word] = [word]
            else:
                hash[sorted_word].append(word)
                
        for key, val in hash.items():
            if len(val) >= 2:
                res += val
        
        return res
