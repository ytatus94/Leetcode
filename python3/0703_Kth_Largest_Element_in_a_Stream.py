# 方法 1. 很慢
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k - 1]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 方法 2. 用 heap 比較快
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        # python 的 heap 是 min heap 由小排到大
        heapq.heapify(self.minHeap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # 插入 val 到正確的位置
        while self.k < len(self.minHeap):
            heapq.heappop(self.minHeap) # 會 pop 最前面的
        return self.minHeap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
