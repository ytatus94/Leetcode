class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        result = []

        # 開一個 hash map 紀錄 p 中每個字母出現的次數
        hash = {}
        for ch in p:
            if ch in hash.keys():
                hash[ch] += 1
            else:
                hash[ch] = 1

        # 用 sliding window 檢查範圍內的字母出現的次數
        # 如果和 p 出現的次數一樣，那就是找到 anagram
        # 因為 sliding window 一次右邊新增一個字母，左邊刪除一個字母
        # 如果新增的字母在 p 內存在，就把 hash 減ㄧ
        # 如果刪除的字母在 p 內存在，就把 hash 加一
        # 當 hash 內都是 0 就表示找到了 anagram

        # 先看 s 開頭，和 p 長度一樣的子字串
        for i in range(len(p)):
            if s[i] in hash.keys():
                hash[s[i]] -= 1

        for i in range(len(s) - len(p) + 1):
            # 當 i = 0 時，什麼都不做，直接檢查 hash
            if i > 0:
                out_ch = s[i - 1] # 離開 sliding window 的字母
                in_ch = s[i + len(p) - 1] # 新加入 sliding window 的字母
                if out_ch in hash.keys():
                    hash[out_ch] += 1
                if in_ch in hash.keys():
                    hash[in_ch] -= 1

            if all(v == 0 for v in hash.values()):
                result.append(i)

        return result
