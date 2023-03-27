# 座標+狀態型 DP, 存在型 DP
# 轉移方程
# f[i][j] = f[k][j-1] or f[k][j] or f[k][j+1] | ak = ai - j
# f[i][j] 是否能最後一跳長度 j 跳到石頭 a_{i}
# 初始條件
# f[1][1] = True 第一顆石頭一定是從第 0 顆石頭以長度為 1 跳過來的
# f[1][j>1] = False 其他長度都不可能從第 0 顆石頭跳到第 1 顆石頭上
# TC = O(N^2), SC = O(N^2) 不能用滾動數組優化，因為最後一跳 f[i][j] 依賴前面的任何一個 f[h][k]

from typing import (
    List,
)

class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def can_cross(self, stones: List[int]) -> bool:
        # write your code here
        if stones is None:
            return False
        n = len(stones)
        # 只有一顆石頭當然是 True
        if n == 1: 
            return True

        # f[i][j] = 從上一顆石頭跳長度 j 的距離能不能跳到石頭 i
        # 假設上一顆石頭是 k, 要跳到 k 可能的長度有 j-1, j, j+1
        # f[i][j] = f[k][j-1] or f[k][j] or f[k][j+1] | ak = ai - j
        # 初始條件
        # f[1][1] = True # 跳到第一顆石頭 (index=0) 的長度是 1
        # f[1][j>1] = False # 所有比 1 大的跳耀長度，都不可能跳到第一顆石頭
        # 邊界情況
        # 如果只有一顆石頭，就是 True
        # 如果 f[n-1][1],...,f[n-1][n-1] 中有一個是 true 那就是能跳到最後一顆石頭 n-1
        # 這時 TC = O(N^2), SC = O(N^2)

        # 用上面的方式求得所有的 f[i][j] 中，大部分都是 False 只有少數 True
        # 這些 False 佔用了大量的空間，效率低
        # 換角度思考，如果 f[k][j] = True，那能跳到的下個距離是 ak+j-1, ak+j, ak+j+1
        # 如果這三個距離上面有石頭，表示能跳到下一顆石頭
        # 所以開一個 Si 集合來存所有能跳到石頭 i 的距離 L
        # 那在這一顆石頭上，下一跳一定是 L-1, L, L+1 的距離，檢查這三個距離有沒有石頭
        # 如果有石頭 j，就把距離加入到 Sj 中 

        # 開一個 hash map 存結果
        # 如果跳了 j 的距離後剛好是石頭 i, 那 Si = {j} 
        # 用 hash 是 O(1) 的查找，可以在 O(1) 的時間內知道有沒有石頭 
        f = {}
        # initialization
        for i in range(n):
            # 每個石頭對應到一個 hash set
            # key 是石頭的下標, value 是能跳到該石頭的距離形成的集合 Si
            f[stones[i]] = set()

        # initial condition
        f[stones[0]].add(0) # 第 0 顆石頭不用跳

        for i in range(n):
            # Si: 保存所有能跳到石頭 i 的所有 j
            si = f[stones[i]]
            # 看所有能跳到石頭 i 的 j 值
            for k in si:
                # ｋ是上一跳的距離, j 是所有可能的下一跳的距離
                for j in [k - 1, k, k + 1]:
                    if j <= 0:
                        continue

                    # 從石頭 i 跳了 j 的距離後，有石頭存在
                    # 就把該石頭和該跳耀距離加入 f
                    if stones[i] + j in f.keys(): # 判斷有沒有石頭存在
                        f[stones[i] + j].add(j)

        if stones[n - 1] in f.keys():
            if len(f[stones[n - 1]]) > 0:
                return True
        return False
