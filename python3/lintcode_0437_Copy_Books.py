# lintcode 437
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        # 一個人花一分鐘抄一頁，
        # 如果只由一個人來抄全部的書，就要 sum(pages) 分鐘
        # 因為一本書是由一個人來抄，抄完一本書所需要的最多的時間是 max(pages) 分鐘
        # 把全部的書抄完，所需要的時間就是 max(pages) ~ sum(pages) 分鐘之間
        #
        # 因為 3 本書分別有 3, 2, 4 頁，由三個人來抄會最快，一個人抄一本
        # 當最後一本書抄完時，共費時 4 分鐘 (最短時間)
        # 由一個人來抄會最慢，全部抄完要 3+2+4 = 9 分鐘 (最長時間)
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_last_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.get_last_people(pages, start) <= k:
            return start
            
        return end
        
    def get_last_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
        
        return count + 1

# 劃分型 DP, 最值型 DP
# 轉移方程
#   f[k][i] = min_{0<=j<=i}( max( f[k-1][j], A[j]+...+A[i-1] ) )
#   f[k][i] = 前 k 個人最少用多少時間抄完前 i 本書
#   f[k-1][j] = 前 k-1 個人最少用多少時間抄完前 j 本書
#   A[j]+...+A[i-1] = 第 k 個人花了多少時間抄第 j~第 i-1 本書
# 初始條件
#   f[0][0] = 0 前 0 個人抄 0 本書費時是 0
#   f[0][1...n] = inf 前 0 個人不可能抄任何書，所以費時無限大
#   f[k][0] = 0 前 k 個人抄 0 本書費時 0
# TC = O(N^2 K), SC = O(NK) 可以優化成 O(N)

from typing import (
    List,
)

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if pages is None:
            return 0
        n = len(pages)
        if n == 0:
            return 0
        if k >= n:
            return max(pages)

        # 開一個數組紀錄
        # f[i][j] = 前 i 個人抄前 j 本書所需要的最短時間
        f = [[float('inf') for i in range(n + 1)] for j in range(k + 1)]

        # 初始條件
        f[0][0] = 0 # 前 0 個人只能抄 0 本書，且費時是 0
        for i in range(1, n + 1):
            f[0][i] = float('inf') # 前 0 個人不能抄任何書

        for i in range(1, k + 1):
            f[i][0] = 0 # 前 i 個人抄 0 本書，費時 0
            for j in range(1, n + 1): # loop 抄一本書到抄 n 本書
                total_time = 0
                for p in range(j, -1, -1): # 要計算抄書所花的時間
                    # 要從後面 loop 可以節省時間複雜度
                    # 當 p = j 的時候 total_time = 0
                    f[i][j] = min(
                        f[i][j],
                        max(f[i - 1][p], total_time)
                    )
                    # 當 j = i 的時候 total_time = 0

                    if p > 0:
                        total_time += pages[p - 1]


        return f[k][n]
        
