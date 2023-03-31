# 序列型 DP, 最值型 DP
# 轉移方程:
#   f[i][0] = min( f[i-1][1]+cost[i-1][0], f[i-1][2]+cost[i-1][0] )
#   f[i][0] = 油漆前 i 棟房子，最後一棟房子 (i-1) 顏色是 0 的最小花費
#   房子的編號是從 0 開始，所以油漆前 i 棟房子，那最後一棟房子的編號是 i-1
#   f[i-1][1] = 油漆前 i-1 棟房子，最後一棟房子 (i-2) 顏色是 1 的最小花費
#   cost[i-1][0] = 當前房子 i-1 漆成顏色 0 的費用
#   需要把各種顏色分開討論
# 初始條件:
#   f[0][0] = f[0][1] = f[0][2] = 0
#   油漆前 0 棟房子，不用任何花費
# TC = O(N), SC = O(N)

from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here

        number_of_houses = len(costs)

        # Create an array to save the minimum cost
        # for painting in 3 different colors
        # We want to know the minimum cost, so we initialize to infinity
        f = [
            [float('inf'), float('inf'), float('inf')] 
            for i in range(number_of_houses + 1)
        ]

        # initialize
        f[0][0], f[0][1], f[0][2] = 0, 0, 0

        # f[i] = minimum cost of painting from house 0 to house i-1 (total i houses)
        # so the for loop starts from 1 (paint 1 house, which house index = 0)
        for i in range(1, number_of_houses + 1):
            f[i][0] = min(f[i-1][1] + costs[i-1][0], f[i-1][2] + costs[i-1][0])
            f[i][1] = min(f[i-1][0] + costs[i-1][1], f[i-1][2] + costs[i-1][1])
            f[i][2] = min(f[i-1][0] + costs[i-1][2], f[i-1][1] + costs[i-1][2])

        return min(f[number_of_houses])

# 改寫一下
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here

        number_of_houses = len(costs)

        # Create an array to save the minimum cost
        # for painting in 3 different colors
        # We want to know the minimum cost, so we initialize to infinity
        f = [
            [float('inf'), float('inf'), float('inf')] 
            for i in range(number_of_houses + 1)
        ]

        # initialize
        f[0][0], f[0][1], f[0][2] = 0, 0, 0

        colors = [0, 1, 2]

        # f[i] = minimum cost of painting from house 0 to house i-1 (total i houses)
        # so the for loop starts from 1 (paint 1 house, which house index = 0)
        for i in range(1, number_of_houses + 1):
            # the current house index = i - 1
            for current_house_color in colors:
                # the cost of painting current house = cost[i-1][current_house_color]
                for previous_house_color in colors:
                    # the color cannot be the same
                    if current_house_color != previous_house_color:
                        f[i][current_house_color] = min(
                            f[i][current_house_color], 
                            f[i-1][previous_house_color] + costs[i-1][current_house_color]
                        )

        return min(f[number_of_houses])
