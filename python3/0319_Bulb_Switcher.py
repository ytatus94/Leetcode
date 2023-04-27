class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        return math.floor(math.sqrt(n))

            
        

# 畫圖可以知道
# 第 i 個燈泡:
# 1. 除了 1 以外的質數燈泡都是關
# 2. 用因數分解就，看有幾個因數來判斷開或關
# ex i = 10: 燈泡的開關是 oxxoxxxxox
# ex i = 20: 燈泡的開關是 oxxoxxxxoxxxxxxoxxxx
# 找出規律 1開 2關 1開 4關 1開 6關 1開 ...
# [1,2,1,4,1,6,1,8,1,10,...]

# 幾個燈泡 亮幾個燈泡
# 1       1
# 4       2
# 9       3
# 16      4
# 25      5
# 36      6
