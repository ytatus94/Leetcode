class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        # 先要做一個字母和 width 對照的 hash table
        hash = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), widths))
        
        unit = 0
        line = 1 # 從第一行開始
        for ch in S:
            if unit + hash[ch] > 100:
                line += 1
                unit = 0
            unit += hash[ch]

        return [line, unit]
