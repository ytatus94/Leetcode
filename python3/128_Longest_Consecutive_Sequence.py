class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 用 DP
        if nums is None or len(nums) == 0:
            return 0

        nums = sorted(nums)
        f = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] - nums[i -1] == 1:
                f[i] = f[i] + f[i - 1]
            elif nums[i] == nums[i - 1]:
                f[i] = f[i - 1]
                
        return max(f)

# lintcode 124
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return 0
            
        # 當只有一個數的時候，最長序列就是 1
        if len(num) == 1:
            return 1
        
        prefix_diff = []
        
        # 先去重，然後排序
        num = sorted(set(num))
        
        # 計算相鄰兩個數的差
        for i in range(1, len(num)):
            prefix_diff.append(num[i] - num[i - 1])
        
        longest = 0
        count = 0
        for i in range(len(prefix_diff)):
            if prefix_diff[i] == 1:
                count += 1
            else:
                # 如果 prefix_diff 中有一個數 != 1
                # 那就把現在的 count 和 longest 做比較，留下最長的，然後把 count 歸零
                longest = max(longest, count)
                count = 0
        
        # 如果 prefix_diff 裡面全都是 1 ，那上面的 else 就不會執行
        # 因此需要這一行來計算 count
        longest = max(longest, count)
        
        # 因為 prefix_diff 是相鄰兩數的差
        # 有 n 組相鄰兩樹的差=1 表示有 n+1 個數，所以要加 1
        return longest + 1
