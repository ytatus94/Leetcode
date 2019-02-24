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

# lintcode 575
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return s
        
        stack = []
        curr_str = ''
        num = 0
        
        # 構成一個 stack = ['str1', 'num2', 'str2', 'num3',...] 的格式
        # 然後 num_i 會重複 str_i 次
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append(curr_str) # 數字之前的字串塞入 stack
                stack.append(num) # 數字塞入 stack
                # 歸零
                curr_str = ''
                num = 0
            elif ch == ']':
                # 遇到 ] 的話，表示目前 stack 裡面最後一個元素一定是數字
                multiplier = stack.pop()
                # stack 中要維持 str, num, str, num 的格式，如果 pop 掉了最後的
                # num ，那 num 前面那個 str 也要一併 pop 出來組成新的字串
                # 因為 num 是對後面的全部 string 做重複
                prev_str = stack.pop()
                curr_str = prev_str + multiplier * curr_str
            else:
                curr_str += ch
        
        return curr_str
