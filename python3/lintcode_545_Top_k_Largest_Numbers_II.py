# lintcode 545
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
