class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = []
        for i in range(1, len(s)):
            if d[s[i - 1]] < d[s[i]]:
                result.append(-1 * d[s[i - 1]])
            else:
                result.append(d[s[i - 1]])
        # 離開迴圈時只把第一個到倒數第二個放到 result
        # 要記得把最後一個加入 result
        result.append(d[s[-1]])

        return sum(result)
