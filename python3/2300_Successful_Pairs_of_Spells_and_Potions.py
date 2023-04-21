class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        result = [0] * n
        nums = sorted(potions)

        for i in range(n):
            target = success / spells[i]

            first_position = self.binary_search(nums, target)

            if first_position != -1:
                result[i] = m - first_position
            else:
                result[i] = 0

        return result

    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid

        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        
        return -1
