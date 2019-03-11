class Solution:
    def findComplement(self, num: int) -> int:
        remainder = [] # 用來保存二進制的每個值
        while num > 0:
            remainder.insert(0, num % 2) # 越早除的餘數會在越右邊
            num //= 2
        
        for i in range(len(remainder)):
            if remainder[i] == 1:
                remainder[i] = 0
            else:
                remainder[i] = 1
        
        complement = 0
        for i in remainder:
            complement = complement * 2 + i
        return complement

class Solution:
        # bin() 會傳回 0b 開頭的二進位，所以要從 index=2 開始才是二進位的數值
        # bin() 傳回的是 str 型態
        binary = bin(num)[2:]
        complement = ''
        for i in range(len(binary)):
            if binary[i] == '0': # 注意是 str 的型態
                complement += '1'
            else:
                complement += '0'
        return int(complement, 2) # 第二個參數是第一個參數的 base
