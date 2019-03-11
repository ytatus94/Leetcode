class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # 先把第一個單字加入 hash table
        hash = {}
        for a in A[0]:
            if a in hash:
                hash[a] += 1
            else:
                hash[a] = 1
        '''
        # 下面這行可以達成同樣的功能
        # 只是型態是 counter 實質上仍是 dictionary
        hash = collections.Counter(A[0])
        '''
        for a in A[1:]:
            for k in hash.keys():
                '''
                如果 key 不在單字裡面，就把 key 移除
                可是在 loop 裡面用 del hash[k] 會 Runtime error
                所以設為 -1
                '''
                if k not in a:
                    hash[k] = -1
                '''
                如果 key 在單字裡面，但是數目比對 hash table 裡的小
                就更新為較小的那個，因為有些字母在某個單字中只出現一次
                在別的單字中出現很多次，例如 cool, lock, cook 中 o 只能算一次
                '''
                count = a.count(k) # 計算 k 在 a 中出現幾次
                if count < hash[k]:
                    hash[k] = count
                    
                '''
                上面可以這樣寫比較簡潔，但是會比較慢
                if k in a:
                    hash[k] = min(hash[k], a.count(k))
                else:
                    hash[k] = -1
                '''
        
        res = []
        for k, v in hash.items():
            if v != -1:
                res += [k] * v
                
        return res
