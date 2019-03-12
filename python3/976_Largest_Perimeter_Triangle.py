class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if A is None or len(A) < 3:
            return 0
        a = sorted(A)
        # i 的下限範圍要滿足 a[i - 2] = a[0] ==> i = 2，所以下限是 1
        for i in range(len(a) - 1, 1, -1):
            print(i, a[i - 2] , a[i - 1] ,a[i])
            if a[i - 2] + a[i - 1] > a[i]:
                return a[i - 2] + a[i - 1] + a[i]
        return 0
