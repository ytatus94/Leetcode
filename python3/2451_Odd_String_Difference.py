class Solution:
    def oddString(self, words: List[str]) -> str:
        if words is None:
            return 0
        m = len(words)
        if m == 0:
            return 0

        hash_map = {}
        for w in words:
            # 確保 j 最大是 len(w)-2, 這樣 j+1 是 len(w)-1 才不會出界
            diff = [ord(w[j + 1]) - ord(w[j]) for j in range(len(w) - 1)]

            # key 可以是 tuple 但不能是 list
            # value 的部分不要計數，直接放入單詞
            if tuple(diff) in hash_map.keys():
                hash_map[tuple(diff)].append(w)
            else:
                hash_map[tuple(diff)] = [w] # 記得用 list

        for k, v in hash_map.items():
            if len(v) == 1:
                return v[0]
        
