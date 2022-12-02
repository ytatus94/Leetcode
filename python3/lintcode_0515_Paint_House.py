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
