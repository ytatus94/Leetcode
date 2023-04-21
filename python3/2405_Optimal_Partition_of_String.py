class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        hash = {}
        for ch in s:
            if ch not in hash.keys():
                hash[ch] = 1
            else:
                # 如果 s[i] 已經存在於 hash 中了，那就重開一個新的 substring
                # 所以 hash 要洗掉重來
                hash = {} # 洗掉
                hash[ch] = 1 # 重來
                result += 1 # 要重開一個新的 substring，所以舊的要計數

        # 離開 for 時，最後一個 substring 沒被result 算入，所以要加一
        return result + 1
