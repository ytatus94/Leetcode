class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if logs is None or len(logs) == 0:
            return logs

        # 先把 logs 分成 letter-logs 和 digit-logs
        digit = []
        letter = []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
                
        '''
        排序 letter-logs
        排序時，照文字順序排序，不考慮 identifier
        但是當文字都一樣的時候，就用 identifier 排序
        所以 identifier 排序要先執行
        '''
        letter.sort(key=lambda x: x.split()[0]) # 用 identifier 排序
        letter.sort(key=lambda x: x.split()[1:]) # 用文字排序
        
        return letter + digit
