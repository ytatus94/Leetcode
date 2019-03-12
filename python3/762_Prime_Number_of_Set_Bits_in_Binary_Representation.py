class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = 0
        for i in range(L, R + 1):
            b = bin(i)[2:]
            count = b.count('1')
            if self.is_prime(count):
                prime += 1
        return prime
    
    def is_prime(self, num):
        if num == 1: # 題目說 1 不算
            return False
        
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
        return True
