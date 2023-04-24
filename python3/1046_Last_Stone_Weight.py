class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones is None or len(stones) == 0:
            return 0

        stones = sorted(stones, reverse=True)

        while len(stones) > 0:
            m1 = stones.pop(stones.index(max(stones)))
            if len(stones) > 0:
                m2 = stones.pop(stones.index(max(stones)))
                if m1 > m2:
                    stones.append(m1 - m2)
            else:
                return m1
        return 0

# 方法2 用 heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones is None or len(stones) == 0:
            return 0

        heap = [-1 * i for i in stones]
        heapify(heap)

        # python 的 heap 是 min heap 就是說 pop 出來的是最小值
        # 所以要把 stones 全都變成負值，這樣 pop 出來的值再變回正值就是最大值

        while len(heap) > 0:
            m1 = heappop(heap) # heap 中的最小值是 stones 中的最大值
            if len(heap) > 0:
                m2 = heappop(heap)
                if m1 < m2: # 注意是 m1 < m2 因為 heap 中是負數
                    heappush(heap, m1 - m2) # heappush 會把 -1*(m1-m2) 放到正確排序後的位置
            else:
                return -1 * m1 # 要變回正數
        return 0
