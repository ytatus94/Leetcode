class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        first = self.findFirstPosition(nums, target)
        last = self.findLastPosition(nums, target)
        return [first, last]
        
    def findFirstPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
    
    def findLastPosition(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1

# 一模一樣的方法，加上解釋
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        starting_position = self.find_first_position(nums, target)
        ending_position = self.find_last_position(nums, target)
        return [starting_position, ending_position]
    
    def find_first_position(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                # start ... mid=target ... end
                # 可能在 start 和 mid 之間還有 target，所以要移動 end
                end = mid
            if nums[mid] > target:
                # start ... target ... mid ... end
                end = mid
            elif nums[mid] < target:
                # start ... mid ... target ... end
                start = mid
                
        if nums[start] == target:
            # 因為要找第一個，所以先比對 start
            return start
        if nums[end] == target:
            return end
        
        return -1
        
    def find_last_position(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                # start ... mid=target ... end
                # 可能在 end 和 mid 之間還有 target，所以要移動 start
                start = mid
            if nums[mid] > target:
                # start ... target ... mid ... end
                end = mid
            elif nums[mid] < target:
                # start ... mid ... target ... end
                start = mid
                
        if nums[end] == target:
            # 因為要找最後一個，所以先比對 end
            return end
        if nums[start] == target:
            return start
        
        return -1
