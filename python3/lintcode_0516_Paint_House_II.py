# 序列型, 最值型
# 如果依照和 paint house 一樣的方式 TC = O(NK^2) 會超時
# 藉由紀錄最小值與次小值，可以將 TC 優化成 TC = O(NK)

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
                
