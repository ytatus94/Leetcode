# 用 quick sort 會超時，因為 quick sort 最好的時候 TC=O(NlogN)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return

        left = start
        right = end
        mid = (start + end) // 2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)
    
# 用 merge sort TC = O(NlogN) 不會超時
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        temp = [0 for _ in range(len(nums))]
        self.merge_sort(temp, nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, temp: List[int], nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return

        mid = (start + end) // 2
        
        self.merge_sort(temp, nums, start, mid)
        self.merge_sort(temp, nums, mid+1, end)
        self.merge(temp, nums, start, mid, end)

    def merge(self, temp, nums, start, mid, end):
        left = start
        right = mid + 1
        idx = start

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[idx] = nums[left]
                left += 1
            else:
                temp[idx] = nums[right]
                right += 1
            idx += 1
        while left <= mid:
            temp[idx] = nums[left]
            left += 1
            idx += 1
        while right <= end:
            temp[idx] = nums[right]
            right += 1
            idx += 1

        for i in range(start, end+1):
            nums[i] = temp[i]

