class Solution:
    # 很慢
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # 先找出 C 在 S 中的 index
        index = []
        for i, v in enumerate(S):
            if v == C:
                index.append(i)
        '''
        其他字母是什麼字母根本沒關係，只是要看每個字母和 e 的最小位移是多少
        先初始化成一個很大的值
        其實初始化成字串長度就夠了
        '''
        res = [len(S) for i in S]
        for e in index:
            res[e] = 0 # e 不會和自己比到，所以要手動設成 0
            i, j = 1, 1
            # 往左邊看
            while e - i > -1:
                res[e - i] = min(res[e - i], i)
                i += 1
            # 往右邊看
            while e + j < len(S):
                res[e + j] = min(res[e + j], j)
                j += 1
        return res

class Solution:
    # 快了一點
    def shortestToChar(self, S: str, C: str) -> List[int]:
        size = len(S)
        res = [size] * size
        C_idx = size # 用來保存 C 的 index
        
        # 由左向右走一次
        for i, v in enumerate(S):
            if v == C:
                res[i] = 0
                C_idx = i
            else:
                if i - C_idx > 0: # 只更新 C_idx 後面的元素的結果
                    res[i] = min(res[i], i - C_idx)
            
        # 由右向左走一次
        for i in range(size - 1, -1, -1):
            if S[i] == C:
                res[i] = 0
                C_idx = i
            else:
                if C_idx - i > 0: # 只更新 C_idx 前面的元素的結果
                    res[i] = min(res[i], C_idx - i)

        return res
