class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        '''
        要讓 B max - B min 越小越好
        所以 B max 要越小，B min 要越大
        由 example 3 知每個元素加上的 x 可以不同，只要 -K <= x <= K 就好
        先計算 A max 和 A min 之間的差 delta
        因為 x 容許的區間有 2K 這麼大
        如果 delta <= 2K 那必定存在一組 x 列表使 B max - B min = 0
        如果 delta > 2K 那 B max - B min = delta - 2K
        '''
        delta = max(A) - min(A)
        if delta > 2 * K:
            return delta - 2 * K
        else:
            return 0
