class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        # 用雙指針一頭一尾，指向的兩個數相加和 target 比較
        # 小+大 > target ==> 大的指針左移一格
        # 小+大 < target ==> 小的指針右移一格
        start = 0
        end = len(nums) - 1
        while (start < end):
            total = nums[start] + nums[end]
            if total == target:
                return [start + 1, end + 1] # 注意要傳回的是 non zero-based index
            elif total > target:
                end -= 1
            else:
                start += 1

        return [] # 如果退出迴圈了都找不到時
