# 博弈型 DP, 存在型 DP
# 轉移方程
#   f[i] = True 當 f[i-1] = False and f[i-2] = False
#   f[i] = True 當 f[i-1] = True and f[i-2] = False
#   f[i] = True 當 f[i-1] = False and f[i-2] = True
#   f[i] = False 當 f[i-1] = True and f[i-2] = True
#   f[i] = 當硬幣數目為 i 的時候，是處於會輸 False 還是會贏 True 的狀態
# 初始條件
#   f[0] = False, f[1] = True
# TC = O(N), SC = O(N) 可以用滾動數組優化到 O(1)

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def first_will_win(self, n: int) -> bool:
        # write your code here
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True

        # A B兩人A先攻B後攻
        # 畫圖解析可以得到
        # 1. 當 A 不管怎麼取，下一步 B 一定會贏 --> 此時的狀態是 A 必輸
        #    同理，當 B 不管怎麼取，下一步 A 一定會贏時，此時的 B 是必輸的狀態
        # 2. 當 A 取一枚和取兩枚硬幣，下一步 B 可能會贏，或可能會輸，
        #    當然 A 會選擇取能讓 B 輸的數目
        # 所以由歸納法得知
        # 1. 不論怎麼取，下一步都是輸 --> 現在必贏
        #    下一步 win or win --> 這一步 lose
        # 2. 不論怎麼取，下一步有可能輸也可能贏 --> 現在必贏 (因為必定會選擇讓下一步輸的取法)
        #    下一步 win or lose --> 這一步 win

        # 開一個數組紀錄目前硬幣數目對應的輸贏
        # f[i] = 目前有 i 枚硬幣，取了一枚或兩枚後會造成贏 True 或輸 False
        f = [False for i in range(n + 1)]

        # f[i] = True if
        # 1. f[i-1] = False and f[i-2] = Fase
        #    f[i] 狀態下，不管拿幾個都會讓下個狀態輸
        # 2. f[i-1] = True and f[i-2] = False
        #    f[i] 狀態下，拿兩個會讓下個狀態變成會輸的狀態 f[i-2] 
        # 3. f[i-1] = False and f[i-2] = True
        #    f[i] 狀態下，拿一個會讓下個狀態變成會輸的狀態 f[i-1]
        # f[i] = False if f[i-1]=True and f[i-2] = True

        # 初始狀態 
        f[0] = False # 沒硬幣了就是輸
        f[1] = True # 只有一個硬幣，取走一個就贏了
        
        for i in range(2, n + 1):
            f[i] = False if f[i-1] and f[i-2] else True

        # 印出來順序
        # for i in range(n + 1):
        #     print(f'step {i} = {f[i]}')

        return f[n]
