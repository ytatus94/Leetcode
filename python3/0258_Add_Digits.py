# 方法 1. 用 str 計算，很慢
class Solution:
    def addDigits(self, num: int) -> int:
        result = [int(i) for i in str(num)]
        while len(result) > 1:
            result = [int(i) for i in str(sum(result))]
        return result[0]

# 方法 2. 用數值做計算
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            total = 0 # 每一輪的和，3+8=11 下一輪要看 1+1=2 所以每一輪要從 0 開始
            while num:
                total += num % 10
                num = num // 10 
            num = total
        return num

# 方法 3. 也是用 str 操作
class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            total = 0
            for i in num_str:
                total += int(i)
            num_str = str(total)
        return int(num_str)
