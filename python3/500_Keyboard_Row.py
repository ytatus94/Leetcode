class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # 分成三個群組，用 set() 會把每個字母變成一個元素，比較方便
        k1 = set('qwertyuiop')
        k2 = set('asdfghjkl')
        k3 = set('zxcvbnm')

        res = []
        for word in words:
            # 先變小寫，然後去重，在轉換成 list 因為 set 不支援 index 操作
            w = list(set(word.lower()))
            
            # 判斷要用哪一個 k 來做比較
            k = None
            if w[0] in k1:
                k = k1
            elif w[0] in k2:
                k = k2
            elif w[0] in k3:
                k = k3
                
            flag = True
            for c in w[1:]:
                if c not in k:
                    flag = False
                    break
                    
            if flag:
                res.append(word)
                
        return res
