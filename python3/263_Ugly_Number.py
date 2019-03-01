# lintcode 517
class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num):
        # write your code here
    
        # ugly number 的因數只包含 2, 3, 5
        # 因為 5 最大就先除以 5，讓 num 變小
        while num >= 5 and num % 5 == 0:
            num //= 5
        # 離開迴圈時 num 可能比 5 小，或是非 5 的倍數
        # 但仍可能是 2 或 3 的倍數
        
        while num >= 3 and num % 3 == 0:
            num //= 3
        # 離開迴圈時 num 可能比 3 小 或非 3 的倍數
        # 但仍可能是 2 的倍數
        
        while num >= 2 and num % 2 == 0:
            num //= 2
        # 離開迴圈時 num 可能比 2 小 或非 2 的倍數
        
        # 會執行到這裡時，num 要麻等於 1 了，要麻就不是 2, 3, 5 的倍數
        if num == 1:
            return True
        return False
