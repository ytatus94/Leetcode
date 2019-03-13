class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        '''
        A = [x1, x2, ..., xn]
        B = [y1, y2, ..., ym]
        sum(A) - xi + yj = sum(B) - yj + xi = [sum(A) + sum(B)] / 2
        所以要找到 2(yj - xi) = sum(B) - sum(A) 的組合
        yj = xi + [sum(B) - sum(A)] // 2
        '''
        delta = sum(B) - sum(A)
        B = set(B) # 去重
        for a in A:
            b = a + delta // 2
            if b in B:
                return [a, b]
        return []
