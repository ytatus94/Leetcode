class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        word_set = set(wordList) # 很重要！一定要先轉成 set!
        queue = [(beginWord, 1)] # 自己本身的距離也要算
        
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, dist+1))
                        word_set.remove(new_word)
                        
        return 0

class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        # 如果沒有先轉換成 set 的話，會一直超時
        word_set = set(wordList)
        
        # 當 word_set 是空的時候 beginWord 是不可能變成 endWord 的
        if len(word_set) == 0:
            return 0
        # 當 beginWord 和 endWord 相同時，不用變就是結果了
        if beginWord == endWord:
            return 1
        
        # 標準的 BFS
        # 1. 把起點放到 queue 並且設一個 hash map 與 queue 同步處理
        queue = [beginWord]
        hash_set = set([beginWord]) # 用來記錄使用過的單字
        
        distance = 0 # 用來記錄單字變了幾次，自己本身要算一次
        
        # 2. 不斷的從 while 迴圈中把 queue 的內容彈出來
        while queue:
            distance += 1
            for i in range(len(queue)): # 層級遍歷
                curr_word = queue.pop(0)
                # 如果已經是 end 了就回傳
                if curr_word == endWord:
                    return distance
                # 改變一個字母之後，可以形成的單字
                for new_word in self.get_new_words(curr_word):
                    # 新的單字要是字典裡面的單字
                    if new_word not in word_set:
                        continue
                    # 新的單字必須是尚未使用過的
                    if new_word in hash_set:
                        continue
                    queue.append(new_word)
                    hash_set.add(new_word)

        return 0
    
    def get_new_words(self, word):
        new_words = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + ch + word[i+1:]
                new_words.append(new_word)
        return new_words
