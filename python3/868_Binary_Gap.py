class Solution:
    def binaryGap(self, N: int) -> int:
        # 先把 N 轉成二進制
        binary = []
        while N > 0:
            binary.insert(0, N % 2)
            N //= 2
        # 記錄下每個 1 的 index
        indexes = []
        for i, v in enumerate(binary):
            if v == 1:
                indexes.append(i)
        # 計算兩個 1 之間的距離，保存最大的距離
        distance = 0
        for i in range(len(indexes) - 1):
            distance = max(distance, indexes[i + 1] - indexes[i])
        return distance

class Solution:
    def binaryGap(self, N: int) -> int:
        # 更快的方法
        ind = [i for i, v in enumerate(bin(N)) if v =='1']
        return max([(b - a) for a, b in zip(ind, ind[1:])] or [0])
