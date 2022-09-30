class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ''' Too slow
        def valid(substr):
            # 如果字串長度和 set 的長度相等，表示沒有重複字元
            return len(substr) == len(set(substr))

        longest = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]

                if valid(substr):
                    size = len(substr)
                    if size > longest:
                        longest = size
        return longest
        '''
        
        # 把每個字元的位置記錄下來
        location = {}
        for c in s:
            location[c] = -1 #initialization

        longest = 0
        curr_str = ''
        for i in range(len(s)):
            c = s[i]
            at = location[c] # 取出字元的位置
            
            # 1. the current char appears for the first time
            if at == -1:
                curr_str += c
                location[c] = i
                continue
            
            idx = curr_str.find(c)
            # 2. the current char is not part of the current string
            if idx == -1: # -1 表示沒有找到時
                curr_str += c
                location[c] = i
            # 3. the current char is part of the current string
            else:
                if longest < len(curr_str):
                    longest = len(curr_str)
                # 有重複字元出現了，所以 curr_str 要從新開始
                curr_str = curr_str[idx+1:] + c
                location[c] = i
                
        # 當迴圈跑完時，還剩下最後一段 curr_str 也要記得比較一下長度
        if len(curr_str) > longest:
            longest = len(curr_str)
        
        return longest
