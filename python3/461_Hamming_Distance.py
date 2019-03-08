class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 把十進制轉換成二進制就是每次都除以二然後看餘數是多少
        # 越早除的餘數放在越右邊
        # 8/2 = 4...0, 4/2 = 2...0, 2/2 = 1...0, 1/2 = 0...1
        # 所以要寫成 1000
        
        if x == y:
            return 0
        
        # 相當於每除以 2 一次，寫成二進制時，餘數就會往左邊移動一格
        # 所以每次除以 2 的時候比較是否餘數相同
        distance = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                distance += 1
            x //= 2
            y //= 2
        
        return distance
    
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 方法二:
        return bin(x^y).count('1')
