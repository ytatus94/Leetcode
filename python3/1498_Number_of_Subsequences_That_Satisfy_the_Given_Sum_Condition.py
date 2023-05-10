class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = 0
        
        # 用雙指針，找出符合條件的 nums[left], nums[right]
        # 從 left + 1 到 right 之間有 right - (left + 1) + 1 = right - left 個數
        # 每個數可以選也可以不選，所以總共有 2^(right - left) 種可能

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow(2, right - left)
                left += 1 # 以 nums[left] 開頭且符合條件的子序列算完了，看下一個數
            else:
                right -= 1 # 目前的 nums[right] 太大了，要找小一點的

        return result % (10**9 + 7) # 題目說要傳回 modulo
