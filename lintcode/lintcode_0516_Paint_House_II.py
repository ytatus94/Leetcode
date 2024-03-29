# 序列型 DP, 最值型 DP
# 轉移方程:
#     f[i][j] = min_{k!=j}(f[i-1][j]) + cost[i-1][j]
#     f[i][j] = 油漆前 i 棟房子且最後一棟房子 (i-1) 的顏色是 j 的最小花費
#     min_{k!=j}(f[i-1][j]) = 油漆前 i-1 棟房子且最後一棟房子 (i-2) 的顏色是 k (k!=j) 的最小花費
# 初始條件:
#     f[0][all colors] = 0 油漆前 0 棟房子 (i.e 表示沒有油漆任何房子) 的最小花費
# 如果依照和 paint house 一樣的方式 TC = O(NK^2) 會超時
# 藉由紀錄 f[i-1][j] 的最小值與次小值，可以將 TC 優化成 TC = O(NK)

# 方法 1: 會超時 TC=O(NK^2)
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        # write your code here
        n = len(costs) # number of houses
        if n == 0:
            return 0
        k = len(costs[0]) # number of colors
        if k == 0:
            return 0

        # Create a num_of_houses x num_of_colors array
        # f[i][j] = minimum cost of painting the first i houses 
        # and the color of house i-1 is j
        f = [[float('inf') for j in range(k)] for i in range(n + 1)]

        # initialize
        for j in range(k):
            f[0][j] = 0 # paint the firs 0 house cost 0

        for i in range(1, n + 1):
            if k > 1:
                for j in range(k): # color of current house i
                    for c in range(k): # color of previous house i-1
                        if c != j:
                            f[i][j] = min(f[i][j], f[i - 1][c] + costs[i - 1][j])
            else:
                f[i][j] = costs[i - 1][j]

        print(f)
        return min(f[n])
                
# 方法 2: 用滾動數組，只記錄 f[i-1][j] 的最小值和次小值
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        # write your code here
        n = len(costs) # number of houses
        if n == 0:
            return 0
        if n == 1: # 注意只有一棟房子時的情形
            return min(costs[0])
        
        k = len(costs[0])

        # Create a num_of_houses x num_of_colors array
        # f[i][j] = minimum cost of painting the first i houses 
        # and the color of house i-1 is j
        f = [[float('inf') for j in range(k)] for i in range(n + 1)]

        # initialize
        for j in range(k):
            f[0][j] = 0 # paint the firs 0 house cost 0

        # Need to know the smallest and second smallest value and their ids
        id1, id2 = 0, 0
        min1, min2 = float('inf'), float('inf')

        for i in range(1, n + 1):
            # find the smallest and second smallest for current i
            min1, min2 = float('inf'), float('inf')
            for j in range(k):
                if f[i - 1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = f[i - 1][j]
                    id1 = j
                elif f[i - 1][j] < min2:
                    min2 = f[i - 1][j]
                    id2 = j

            # loop all color
            for j in range(k):
                f[i][j] = costs[i - 1][j]
                if j != id1:
                    f[i][j] += min1 
                else:
                    f[i][j] += min2

        return min(f[n])

    
# 改寫一下滾動數組
# 最小值和次小值，還有對應的顏色應該放到 for i in range(1, n+1) 才對
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        # write your code here
        n = len(costs)
        if n == 0:
            return 0

        if n == 1:
            return min(costs[0])

        k = len(costs[0])
        if k == 0:
            return 0

        dp = [[float('inf') for j in range(k)] for i in range(n + 1)]

        for j in range(k):
            dp[0][j] = 0

        for i in range(1, n + 1):
            min_cost1 = float('inf')
            min_cost2 = float('inf')
            min_color1 = 0
            min_color2 = 0
            for j in range(k):
                if dp[i - 1][j] < min_cost1:
                    min_cost2 = min_cost1
                    min_cost1 = dp[i - 1][j]
                    min_color2 = min_color1
                    min_color1 = j
                elif dp[i - 1][j] < min_cost2:
                    min_cost2 = dp[i - 1][j]
                    min_color2 = j

            for j in range(k):
                if j != min_color1:
                    dp[i][j] = min_cost1 + costs[i - 1][j]
                else:
                    dp[i][j] = min_cost2 + costs[i - 1][j]

        return min(dp[n])
