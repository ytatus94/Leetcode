class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            temp = num
            while temp != 0:
                divide = temp % 10 # 求出每一位數
                # 不包含有 0 的數，
                if divide == 0 or num % divide != 0:
                    break
                temp //= 10
            # 離開迴圈時，如果不是 break 的話，是正常結束的話 temp 會等於 0
            if temp == 0:
                res.append(num)
            
        return res
