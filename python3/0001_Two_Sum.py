class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, val in enumerate(nums):
            if target - val in hash_map:
                return [hash_map[target - val], idx]
            else:
                hash_map[val] = idx
                
# lintcode 56
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash_map = {}
        for idx, val in enumerate(numbers):
            if target - val in hash_map:
                return [hash_map[target - val], idx]
            else:
                hash_map[val] = idx
