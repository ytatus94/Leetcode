class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        multiplier = ''
        stack.append([0, '']) # 要有這一個，這樣單層的情況才不會出錯

        for c in s:
            # 抓出數字來
            if c.isdigit():
                multiplier += c
            elif c == '[':
                record = [int(multiplier), ''] # multiplier 要轉成整數，pattern 的部分暫時用空字串取代
                stack.append(record)
                multiplier = '' # 要把 multiplier 清空，塞入下一個數字時才不會出錯
            elif c == ']':
                mul, pattern = stack.pop()
                decoded = pattern * mul # 內層的字串長這樣
                last_record = stack[-1]
                last_record[1] += decoded # 把內層字串塞給上一層
            else: # 處理 string pattern
                curr_record = stack[-1] # 取出最後一個紀錄，是一個 list
                curr_record[1] += c # 紀錄 list 內的第二個元素才是字串

        return stack[0][1]
