class Solution:
    def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        # 先把 wordList 變成一個 set() 移除掉重複的單字
        word_set = set(wordList)
        
        # 如果 beginWord 在 word_set 裡面，就刪掉 beginWord
        if beginWord in word_set:
            word_set.remove(beginWord)
        # 如果 endWord 不在 word_set 裡面，就結束
        if endWord not in word_set:
            return []
        
        res = []
        dist = {node:0 for node in word_set} # 用來記錄每個點和 beginWord 的距離
        
        # 用 BFS 先找出最短路徑，記錄下每個點與 beginWord 的距離
        self.bfs(beginWord, endWord, word_set, dist)
        print(dist)
        # 在用 DFS 從 endWord 出發往 beginWord 走，每走一步距離就必須要變近一點
        self.dfs(beginWord, endWord, dist, res, [endWord])
        
        return res
    
    def bfs(self, beginWord, endWord, word_set, dist):
        queue = [(beginWord, 0)] # 第二個參數是和起點的距離
        while queue:
            word, d = queue.pop(0)
            dist[word] = d
            if word == endWord: # 找到了就回傳
                return
            # 新的單字是舊的單字改變一個字母
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in word_set: # 必須要是字典裡面的單字
                        queue.append((new_word, d + 1))
                        word_set.remove(new_word) # 要從字典裡拿掉才不會出錯
                    
    def dfs(self, beginWord, endWord, dist, res, path):
        last_word = path[-1]
        if last_word == beginWord:
            res.append(path[::-1]) # 因為是從 endWord 出發，所以最後 path 要反轉
            return
        for k, v in dist.items():
            # 要從 endWord 往 beginWord 走，所以和 beginWord 的距離會越來越小
            if v != dist[last_word] - 1:
                continue
            diff = 0 # 紀錄 k 和 last_word 有幾個字母不同
            for i in range(len(last_word)):
                if k[i] != last_word[i]:
                    diff += 1
            if diff > 1: # 不相同的字母大於一個時，就不是我要找的
                continue
            path.append(k)
            last_word = k
            self.dfs(beginWord, endWord, dist, res, path)
            path.pop()
            last_word = path[-1]
