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

# 方法2: 速度慢很多
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

# lintcode 457
class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
