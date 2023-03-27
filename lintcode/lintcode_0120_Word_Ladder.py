# lintcode 120
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if end not in dict:
            dict.add(end)
            
        queue = [(start, 1)]
        
        while queue:
            word, dist = queue.pop(0)
            if word == end:
                return dist
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in dict:
                        queue.append((new_word, dist+1))
                        dict.remove(new_word)
        
        return 0
        
class Solution:
    def ladderLength(self, start, end, dict):
        if len(dict) == 0:
            return 0
        
        if start == end:
            return 1
        
        if end not in dict:
            dict.add(end) # dict 是一個 set() 所以用 add()
        
        queue = [start]
        hash_set = set([start]) # 不知道為什麼要用 set() 才不會超時
        length = 0
        
        while queue:
            length += 1
            for i in range(len(queue)): # 層級遍歷
                word = queue.pop(0)
                if word == end:
                    return length
                for new_word in self.get_next_word(word, dict):
                    if new_word in hash_set: # 已經用過的單字不可再使用
                        continue
                    queue.append(new_word)
                    hash_set.add(new_word)
        return 0
        
    def get_next_word(self, word, dict):
        new_words = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == ch:
                    continue
                new_word = word[:i] + ch + word[i+1:]
                if new_word in dict:
                    new_words.append(new_word)
        return new_words
