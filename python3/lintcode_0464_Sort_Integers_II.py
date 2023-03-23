# 用 Merge Sort
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        # write your code here
        temp = [None for i in range(len(a))] # 需要用來記錄排序好的部分
        self.merge_sort(a, 0, len(a) - 1, temp)

    def merge_sort(self, a: List[int], start: int, end: int, temp: List[int]):
        if start >= end:
            return
        mid = (start + end) // 2 # 要求中間點

        # 先不斷地左右拆分
        self.merge_sort(a, start, mid, temp)
        self.merge_sort(a, mid + 1, end, temp)
        # 拆分完後要排序，然後合併
        self.merge_array(a, start, mid, end, temp)

    def merge_array(self, a: List[int], start: int, mid: int, end: int, temp: List[int]):
        left = start
        right = mid + 1
        idx = start

        while left <= mid and right <= end:
            if a[left] <= a[right]:
                temp[idx] = a[left]
                left += 1
            else:
                temp[idx] = a[right]
                right += 1
            idx += 1

        # 如果還有剩下的，就把剩下的加入
        while left <= mid:
            temp[idx] = a[left]
            left += 1
            idx += 1
        while right <= end:
            temp[idx] = a[right]
            right += 1
            idx += 1
        # 因為目前只有 start 到 end 排序好了
        # 所以只要把 start 到 end 的部分寫入 a 就好
        for i in range(start, end + 1):
            a[i] = temp[i]

# 用 quick sort
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        # write your code here
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, a: List[int], start: int, end: int):
        if start >= end:
            return

        left = start
        right = end

        # 用中間點當 pivot
        mid = (start + end) // 2
        pivot = a[mid]

        # quick sort 用 left <= right (有等號) 不是用 left < right
        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                temp = a[left]
                a[left] = a[right]
                a[right] = temp
                left += 1
                right -= 1

        # 離開 while loop 時，一定是這種格式 start .... right left ... end
        # 就是 right 在 left 左邊了
        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)
