# lintcode 545
# 會超時
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        # 用 min heap 只保存 k 個數
        # 當超過 k 個數要放到 heap 裡面的時候，就挑出 heap 裡最小的數
        # 和要放入的數比較，如果 heap 裡最小的數比較小，就刪除，然後把要放入的數放到 heap 中
        # 如果要放入的數比較小，就什麼也不幹，維持原本的 heap
        if len(self.heap) < self.k:
            self.heap.append(num)
        elif num > min(self.heap):
            self.heap.remove(min(self.heap))
            self.heap.append(num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True) # 會超時

# 會超時
class Solution:
    def __init__(self, k):
        self.k = k
        self.nums = []

    def add(self, num):
        if len(self.nums) < self.k:
            self.nums.append(num)
        elif num > min(self.nums):
            self.nums.remove(min(self.nums))
            self.nums.append(num)

    def topk(self):
        if self.k >= len(self.nums):
            return sorted(self.nums, reverse=True)

        start = 0
        end = len(self.nums) - 1
        top = self.quick_select(self.nums, start, end, len(self.nums) - self.k)
        res = []
        for i in self.nums:
            if i > top:
                res.append(i)
        return sorted(res, reverse=True)

    def quick_select(self, nums, start, end, n):
        if start >= end:
            return nums[n]

        left = start
        right = end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if n <= right:
            return self.quick_select(nums, start, right, n)
        if n >= left:
            return self.quick_select(nums, left, end, n)
        return nums[n]

# 用 priority queue 才不會超時
import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.heap = []
        
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        elif num > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True)
