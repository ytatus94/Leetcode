class TwoSum:
    def __init__(self):
        self.nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.nums.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # 這部分就是 two sum = target 經典

        nums = sorted(self.nums)

        start = 0
        end = len(nums) - 1
        
        while (start < end):
            total = nums[start] + nums[end]
            if total == value:
                return True
            elif total > value:
                end -= 1
            else:
                start += 1
        
        return False
