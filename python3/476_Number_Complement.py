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
