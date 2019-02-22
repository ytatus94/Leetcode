class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        while head + 1 < tail:
            mid = head + (tail - head) // 2 # 整數除法
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid
            elif nums[mid] < target:
                head = mid
                
        if nums[head] == target:
            return head
        if nums[tail] == target:
            return tail
        return -1
